#!/usr/bin/python3
"""
Function that inserts a line of text to a file after each line
containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts new_string after each line containing search_string.
    """
    lines = []

    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(lines)
