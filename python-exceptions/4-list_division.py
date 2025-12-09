#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divide elements of my_list_1 by elements of my_list_2 element-wise.

    Returns a list of length list_length containing the division results.
    If division fails, appends 0 instead and prints an error message:
      - "out of range" for IndexError
      - "division by 0" for ZeroDivisionError
      - "wrong type" for non-integer/float values
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
