#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = 0
    p = set(my_list)
    for i in p:
        new += i
    return new
