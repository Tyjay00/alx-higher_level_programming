#!/usr/bin/python3
"""This script defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a text file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
