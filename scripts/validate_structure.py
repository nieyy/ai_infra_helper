#!/usr/bin/env python3
"""Validate the AI Infra Helper artifact structure.

The checks are intentionally lightweight: they prevent common placement,
naming, and staging mistakes without imposing project-specific workflows.
"""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path


ROOT_ALLOWED_DIRS = {".git", "docs", "logs", "patches", "scripts"}
ROOT_REQUIRED_DIRS = {"docs", "logs", "patches", "scripts"}
ROOT_ALLOWED_FILES = {".gitignore", "AGENTS.md", "CLAUDE.md", "README.md"}

BANNED_TOP_LEVEL_DIRS = {
    "artifacts",
    "imports",
    "implementation",
    "misc",
    "outputs",
    "records",
    "state",
    "tmp",
}

DOCS_ALLOWED_DIRS = {
    "designs",
    "rca",
    "research",
    "reviews",
    "runbooks",
    "templates",
    "test-reports",
}
DOCS_REQUIRED_DIRS = DOCS_ALLOWED_DIRS
DOCS_ALLOWED_ASSET_DIRS = {"research": {"assets"}}
ASSET_EXTENSIONS = {".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}

DATED_DOCUMENT_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*-(?:en|zh)\.md$"
)
RUNBOOK_RE = re.compile(r"^[a-z0-9][a-z0-9-]*(?:-(?:en|zh))?\.md$")
TEMPLATE_RE = re.compile(r"^[a-z0-9][a-z0-9-]*-template-(?:en|zh)\.md$")

RAW_EXTENSIONS = {".err", ".log", ".out", ".tar", ".tgz", ".zip"}
PATCH_ARCHIVE_EXTENSIONS = {".tar", ".tar.gz", ".tgz", ".zip"}
MAX_STAGED_FILE_BYTES = 5 * 1024 * 1024
SENSITIVE_NAME_PARTS = {"credential", "password", "passwd", "secret", "token"}
IGNORED_TOP_LEVEL_FILE_SUFFIXES = {".bak", ".swp", ".tmp"}


def run_git(args: list[str]) -> list[str]:
    """Run a Git query, returning no results outside a usable repository."""
    try:
        output = subprocess.check_output(
            ["git", *args], stderr=subprocess.DEVNULL, text=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    return [line for line in output.splitlines() if line]


def staged_files() -> list[str]:
    return run_git(["diff", "--cached", "--name-only", "--diff-filter=ACMRT"])


def has_suffix(path: str, suffixes: set[str]) -> bool:
    lower = path.lower()
    return any(lower.endswith(suffix) for suffix in suffixes)


def validate_root(root: Path, errors: list[str], warnings: list[str]) -> None:
    present_dirs = {path.name for path in root.iterdir() if path.is_dir()}
    for name in sorted(ROOT_REQUIRED_DIRS - present_dirs):
        errors.append(f"missing required top-level directory: {name}/")

    for child in root.iterdir():
        name = child.name
        if child.is_dir():
            if name in BANNED_TOP_LEVEL_DIRS:
                errors.append(f"banned top-level directory exists: {name}/")
            elif name not in ROOT_ALLOWED_DIRS:
                errors.append(f"unknown top-level directory: {name}/")
        elif (
            child.is_file()
            and name not in ROOT_ALLOWED_FILES
            and not any(name.endswith(suffix) for suffix in IGNORED_TOP_LEVEL_FILE_SUFFIXES)
        ):
            warnings.append(f"unexpected top-level file: {name}")


def validate_docs(root: Path, errors: list[str], warnings: list[str]) -> None:
    docs = root / "docs"
    if not docs.is_dir():
        return

    present_dirs = {path.name for path in docs.iterdir() if path.is_dir()}
    for name in sorted(DOCS_REQUIRED_DIRS - present_dirs):
        errors.append(f"missing required docs directory: docs/{name}/")

    for child in docs.iterdir():
        if child.is_dir() and child.name not in DOCS_ALLOWED_DIRS:
            errors.append(f"unknown docs directory: docs/{child.name}/")
        elif child.is_file() and child.name != ".gitkeep":
            errors.append(f"file must be placed in a docs category: docs/{child.name}")

    naming_rules = {
        "runbooks": RUNBOOK_RE,
        "templates": TEMPLATE_RE,
    }
    for category in DOCS_ALLOWED_DIRS:
        category_path = docs / category
        if not category_path.is_dir():
            continue
        pattern = naming_rules.get(category, DATED_DOCUMENT_RE)
        for path in category_path.iterdir():
            if path.is_dir():
                if path.name not in DOCS_ALLOWED_ASSET_DIRS.get(category, set()):
                    errors.append(
                        f"unexpected nested directory: docs/{category}/{path.name}/"
                    )
                    continue
                for asset in path.iterdir():
                    if asset.is_dir():
                        errors.append(
                            f"unexpected nested asset directory: "
                            f"docs/{category}/{path.name}/{asset.name}/"
                        )
                    elif asset.suffix.lower() not in ASSET_EXTENSIONS:
                        errors.append(
                            f"unsupported asset file: "
                            f"docs/{category}/{path.name}/{asset.name}"
                        )
            elif path.name != ".gitkeep" and not pattern.fullmatch(path.name):
                warnings.append(
                    f"non-standard document name: docs/{category}/{path.name}"
                )


def validate_staged(root: Path, errors: list[str]) -> None:
    for path in staged_files():
        parts = Path(path).parts
        if not parts:
            continue

        if parts[0] in BANNED_TOP_LEVEL_DIRS:
            errors.append(f"staged file under banned directory: {path}")

        lower_name = Path(path).name.lower()
        if any(part in lower_name for part in SENSITIVE_NAME_PARTS):
            errors.append(f"staged file has a sensitive-looking name: {path}")

        if path.startswith("logs/") and path != "logs/.gitkeep":
            if has_suffix(path, RAW_EXTENSIONS | {".tar.gz"}):
                errors.append(f"staged raw log or archive: {path}")

        if path.startswith("patches/") and has_suffix(
            path, PATCH_ARCHIVE_EXTENSIONS
        ):
            errors.append(f"staged patch archive; keep a text patch instead: {path}")

        absolute_path = root / path
        if absolute_path.is_file() and absolute_path.stat().st_size > MAX_STAGED_FILE_BYTES:
            errors.append(f"staged file is larger than 5 MiB: {path}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    os.chdir(root)

    errors: list[str] = []
    warnings: list[str] = []
    validate_root(root, errors, warnings)
    validate_docs(root, errors, warnings)
    validate_staged(root, errors)

    if errors:
        print("Structure validation failed:\n")
        for item in errors:
            print(f"ERROR: {item}")
        if warnings:
            print()
            for item in warnings:
                print(f"WARN: {item}")
        return 1

    if warnings:
        print("Structure validation passed with warnings:\n")
        for item in warnings:
            print(f"WARN: {item}")
        return 0

    print("Structure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
