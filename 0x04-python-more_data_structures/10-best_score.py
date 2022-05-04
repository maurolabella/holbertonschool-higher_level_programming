#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keys = list(a_dictionary)
    max = a_dictionary[keys[0]]
    for key in keys:
        if a_dictionary[key] > max:
            max = a_dictionary[key]
    return max
