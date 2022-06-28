#!/usr/bin/python3
def islower(c):
    p = ord(c)
    for i in range(97, 123):
        if p == i:
            return True
        else:
            return False
