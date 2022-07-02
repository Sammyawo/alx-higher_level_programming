#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        p = tuple_a[:2]
    else:
        if len(tuple_a) == 1:
            p = tuple_a[0], 0
        else:
            p = 0, 0

    if len(tuple_b) >= 2:
        d = tuple_b[:2]
    else:
        if len(tuple_b) == 1:
            d = tuple_b[0], 0
        else:
            d = 0, 0

    return (p[0] + d[0], p[1] + d[1])
