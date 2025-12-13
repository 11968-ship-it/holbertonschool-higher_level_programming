#!/usr/bin/python3
"""
5-text_indentation module

This module contains a function that prints a text with 2 new lines after
each of these characters: '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            # Print the text from start to current char, stripped
            print(text[start:i + 1].strip())
            print()  # Extra newline
            start = i + 1

    # Print any remaining text after the last separator
    remainder = text[start:].strip()
    if remainder:
        print(remainder)

