#!/usr/bin/python3
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
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    remainder = text[start:].strip()
    if remainder:
        print(remainder)
