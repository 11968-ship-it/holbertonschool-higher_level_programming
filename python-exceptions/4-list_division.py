#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divide elements of two lists element-wise, printing errors and
    returning a list of length list_length with results or 0 on failure.
    """
    result = []
    for i in range(list_length):
        div = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError
            div = a / b
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            result.append(div)
    return result
