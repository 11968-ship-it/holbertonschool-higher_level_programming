#!/usr/bin/python3
"""Module that defines a function to write text to a file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 file and returns the character count."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
