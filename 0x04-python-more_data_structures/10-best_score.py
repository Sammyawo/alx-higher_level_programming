#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxx = max(a_dictionary.values())
        return [i for i, j in a_dictionary.items() if j == maxx][0]
