#!/usr/bin/python3
for i in range(0, 100):
    if i != 99:
        j = 44
        print("{:02d}{:c} ".format(i, j), end="")
    else:
        print("{:02d}".format(i))
