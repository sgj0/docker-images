#!/usr/bin/env python3

import sys
import os
import json
import re
import semver
import toml
from typing import Optional


def get_version() -> Optional[str]:
    filename = None

    if os.path.exists("package.json"):
        filename = "package.json"
    elif os.path.exists("pyproject.toml"):
        filename = "pyproject.toml"
    else:
        print("File not found.")
        sys.exit(1)

    ext = os.path.splitext(filename)[1].lower()

    try:
        with open(filename, "r", encoding="utf-8") as f:
            if ext == ".json":
                data = json.load(f)
                return data.get("version")
            elif ext == ".toml":
                data = toml.load(f)
                return data["project"]["version"]

    except (IOError, json.JSONDecodeError, toml.TomlDecodeError) as e:
        print(e)
        sys.exit(1)


def update_version_in_file(new_version: str, filepath: str):
    if not os.path.exists(filepath):
        print(f"{filepath} not found.")
        return

    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()

    content_to_write = None

    try:
        if ext == ".json":
            with open(filepath, "r+", encoding="utf-8") as f:
                data = json.load(f)
                data["version"] = new_version
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
            print(f"File updated {filepath}: {new_version}")

        elif ext == ".toml":
            with open(filepath, "r+", encoding="utf-8") as f:
                data = toml.load(f)

                data["project"]["version"] = new_version

                f.seek(0)
                toml.dump(data, f)
                f.truncate()
            print(f"File updated {filepath}: {new_version}")

        elif ext == ".xml":
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            updated_content = re.sub(
                r'(<widget[^>]*?version=)"[^"]*"',
                rf'\1"{new_version}"',
                content,
                count=1,
                flags=re.IGNORECASE | re.DOTALL,
            )

            if updated_content == content:
                print(f" {filepath} (XML).")

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"File updated {filepath}: {new_version}")

    except Exception as e:
        print(f"Error updating  {filepath}: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python versioning.py [major|minor|patch]")
        sys.exit(1)

    level = sys.argv[1].lower()
    if level not in ["major", "minor", "patch"]:
        print("Invalid level: major|minor|patch")
        sys.exit(1)

    current_version_str = get_version()
    if not current_version_str:
        print("No version found.")
        sys.exit(1)

    try:
        current_version = semver.Version.parse(current_version_str)
    except ValueError as e:
        print(e)
        sys.exit(1)

    if level == "major":
        new_version = current_version.bump_major()
    elif level == "minor":
        new_version = current_version.bump_minor()
    elif level == "patch":
        new_version = current_version.bump_patch()

    new_version_str = str(new_version)
    print(f"Actual version: {current_version_str}")
    print(f"New version ({level}): {new_version_str}")

    files_to_update = [
        "package.json",
        "composer.json",
        "server/composer.json",
        "server/package.json",
        "client/package.json",
        "mobile/package.json",
        "mobile/config.xml",
        "pyproject.toml",
    ]

    print("--- Updating files ---")
    for file_path in files_to_update:
        update_version_in_file(new_version_str, file_path)


if __name__ == "__main__":
    main()
