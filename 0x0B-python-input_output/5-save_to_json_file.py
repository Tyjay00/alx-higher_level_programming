#!/usr/bin/python3
"""This script defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write a object to a JSON file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
