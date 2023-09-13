#!/usr/bin/python3
"""This script defines a text file-reading function."""


def read_file(filename=""):
    """Read and print the contents of a text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
