#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return None

    L = my_list[0]
    # for loop method
    # for num in my_list:
    #    if num > L:
    #        L = num
    # while method
    i = 1
    while i < len(my_list):
        if my_list[i] > L:
            L = my_list[i]
        i += 1
    return L
