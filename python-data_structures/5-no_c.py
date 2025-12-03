#!/usr/bin/python3
def no_c(my_string):
    """Return a copy of my_string without 'c' and 'C' characters."""
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
