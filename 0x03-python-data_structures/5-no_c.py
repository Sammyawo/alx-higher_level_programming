#!/usr/bin/python3
def no_c(my_string):
    p = ''
    for i in my_string:
        if i != 'C' and i != 'c':
            p += i
    return p
