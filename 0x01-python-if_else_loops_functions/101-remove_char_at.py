#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        p = str[:n] + str[n + 1:]
    else:
        p = str[:n]
    return p
