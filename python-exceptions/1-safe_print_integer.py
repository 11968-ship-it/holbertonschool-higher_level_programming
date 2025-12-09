#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer using '{:d}'.format().
    Returns True if value is an integer and printed correctly,
    otherwise returns False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
