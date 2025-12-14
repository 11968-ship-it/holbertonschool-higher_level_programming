#!/usr/bin/python3
"""
This module provides a function that prints a text with two new lines
after each '.', '?', and ':' character.

The function ensures that the text is a string and trims spaces
at the beginning and end of each printed line.
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each '.', '?', or ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = {'.', '?', ':'}
    start = 0
    length = len(text)

    for i, char in enumerate(text):
        if char in separators:
            # Extract the segment and strip leading/trailing spaces
            segment = text[start:i + 1].strip()
            if segment:
                print(segment)
                print()
            start = i + 1

    # Print any remaining text after the last separator
    remaining = text[start:].strip()
    if remaining:
        print(remaining)
