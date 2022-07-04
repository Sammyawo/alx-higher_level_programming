#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    p = []
    for i in my_list:
        if i % 2 == 0:
            p.append(True)
        else:
            p.append(False)
    return p
