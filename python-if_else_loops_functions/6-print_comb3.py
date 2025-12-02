#!/usr/bin/python3
for m in range(10):
    for j in range(m + 1, 10):
        if m == 8 and j == 9:
            print(f"{}{}".format(m, j))
        else:
           print(f"{}{}".format(m, j), end=", ")
