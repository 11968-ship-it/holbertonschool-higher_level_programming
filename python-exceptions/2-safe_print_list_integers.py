#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print first x integers of my_list.
    Returns the number of integers printed.
    Raises IndexError if x > len(my_list)."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip non-integers silently
            continue
    print()
    return count
