#!/usr/bin/python3
for i in range(122, 97, -2):
    j = (i - 1) - 32
    print("{:c}{:c}".format(i, j), end="")
