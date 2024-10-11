#! /usr/bin/env python

import sys
import shutil
from pathlib import Path
import re

# Path to STOPS source directory
SRC = Path("/media/justin/Transcend/STOPS/src/STOPS/")

# Relevant source files
FILES = [
    "__main__.py",
    "split.py",
    "join.py",
    "cross_correlate.py",
    "skylines.py",
]

# Regex docstring pattern
class_pattern = re.compile(r'class\s+\w+:\n\s*"""\n(.*?)\n\s*"""\n', re.DOTALL)
doc_pattern = re.compile(r'\s*"""\n(.*?)\n\s*"""\n', re.DOTALL)


def format_docs(docstring: str, indent: int = 4) -> str:
    lines = docstring.split("\n")
    return "\n".join([line[indent:] for line in lines])


def save_docstring(src_file: Path) -> None:
    docstring: str = ""

    with open(src_file, "r") as file:
        content = file.read()

        matches = class_pattern.findall(content)

        if matches := class_pattern.findall(content):
            docstring = format_docs(matches[0])

        elif matches := doc_pattern.findall(content):
            docstring = format_docs(matches[0], indent=0)

        else:
            raise ValueError(f"No class or module docstring found in {src_file.name}")

    with open(src_file.with_suffix(".doc"), "w") as file:
        file.write(docstring)

    return


def main(args):

    # Check STOPS source directory exists
    if not SRC.is_dir():
        return

    # Path to local directory
    dst = Path(args[0]).parent

    # For each source file in SRC
    for file in FILES:

        file = SRC / file

        # Check file exists
        if not file.is_file():
            raise FileNotFoundError(f"{file.name} not found in {file.parent}")

        # Copy file to local directory
        shutil.copy(file, dst / file.name)

        file = dst / file.name

        # Create doc file and extract class docstring
        save_docstring(file)

    return


if __name__ == "__main__":
    main(sys.argv)
