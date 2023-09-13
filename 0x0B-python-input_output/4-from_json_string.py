#!/usr/bin/python3
# 6-from_json_string.py
"""This script defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of the JSON data string."""
    return json.loads(my_str)
