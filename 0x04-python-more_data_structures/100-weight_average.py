#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        w = 0
        r = 0
        for i in my_list:
            w += i[0] * i[1]
            r += i[1]
        y = w / r
    return y 
