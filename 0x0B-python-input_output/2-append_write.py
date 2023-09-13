#!/usr/bin/python3
"""This script defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.

    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
