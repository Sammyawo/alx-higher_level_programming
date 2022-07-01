#!/usr/bin/python3
def new_in_list(my_list, idx, element): 
    lists = my_list[:]
    if idx >= 0 and idx <= len(lists) - 1:
        lists[idx] = element
    return lists
