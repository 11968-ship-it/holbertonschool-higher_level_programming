#!/usr/bin/python3
"""Module that defines a function to append text to a file."""


def append_write(filename="", text=""):
    """Appends a string to a UTF-8 file and returns the character count."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
