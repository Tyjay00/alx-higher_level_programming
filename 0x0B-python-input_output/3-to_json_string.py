#!/usr/bin/python3
"""This script defines a string to a JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of the string object."""
    return json.dumps(my_obj)
