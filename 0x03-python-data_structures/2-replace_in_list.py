#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0:
        for i in range(len(my_list)):
            if idx == i:
                my_list[i] = element
        return my_list
    else:
        return my_list
