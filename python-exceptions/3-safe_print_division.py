#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides a by b, prints the result inside finally,
    returns the result or None.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
