#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    p = []
    if value in a_dictionary.values():
        for i in a_dictionary:
            if a_dictionary[i] == value:
                p += [i]

        for j in p:
            del a_dictionary[j]
    return a_dictionary
