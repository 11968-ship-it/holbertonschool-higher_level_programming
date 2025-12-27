#!/usr/bin/python3
"""
Function that returns the dictionary description of an object
for JSON serialization.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    of an object for JSON serialization.
    """
    return obj.__dict__
