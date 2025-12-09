#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides elements from my_list_1 by my_list_2 element-wise safely.
    Returns a list of length list_length with results or 0 on error.
    Prints errors as specified."""
    result = []
    for i in range(list_length):
        div = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
                raise TypeError
            div = a / b
        except IndexError:
            print("out of range")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0
        finally:
            result.append(div)
    return result
