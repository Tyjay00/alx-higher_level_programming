#!/usr/bin/python3
"""This script converts a Python class to JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
