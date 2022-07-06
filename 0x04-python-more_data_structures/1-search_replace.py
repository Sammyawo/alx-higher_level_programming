#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for i in my_list:
        if i == search:
            new += [replace]
        else:
            new += [i]
    return new
