#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.
    Returns the number of integers printed."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            if isinstance(i, int) and i >= len(my_list):
                break
            continue
    print()
    return count
