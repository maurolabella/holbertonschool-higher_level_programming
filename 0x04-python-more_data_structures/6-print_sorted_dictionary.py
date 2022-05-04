#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for x in list(sorted(a_dictionary)):
        print(f"{x}: {a_dictionary[x]}")
