#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """A custom list class that inherits from the built-in list class.

        This class provides a method, `print_sorted()`, to print the list in
        ascending sorted order."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
