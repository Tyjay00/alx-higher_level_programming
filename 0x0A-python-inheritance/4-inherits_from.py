#!/usr/bin/python3
"""Defines an inherited class-checking function."""

def inherits_from(obj, a_class):
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
