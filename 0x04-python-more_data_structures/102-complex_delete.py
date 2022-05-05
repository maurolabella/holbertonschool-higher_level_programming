#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    tmp = a_dictionary.copy()
    for x in tmp:
        if tmp[x] == value:
            del(a_dictionary[x])
    return a_dictionary
