#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    pack = a_dictionary.copy()
    for i, j in pack.items():
        pack[i] = j * 2
    return pack
