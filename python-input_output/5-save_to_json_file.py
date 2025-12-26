#!/usr/bin/python3
"""Module that defines a function to save an object to a JSON file."""

import json

def save_to_json_file(my_obj, filename):
    """Writes a Python object to a text file in JSON format."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
