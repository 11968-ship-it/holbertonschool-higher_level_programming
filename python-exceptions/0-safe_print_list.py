def safe_print_list(my_list=[], x=0):
    """Print x elements of a list and return the count."""
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
