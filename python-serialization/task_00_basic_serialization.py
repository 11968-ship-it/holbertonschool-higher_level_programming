#!/usr/bin/env python3
"""
Basic serialization module
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Filename of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): Filename of the input JSON file.

    Returns:
        dict: Deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
