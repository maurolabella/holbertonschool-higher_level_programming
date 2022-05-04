#!/usr/bin/python3

def common_elements(set_1, set_2):
    tmp = [element for element 
		in set_1 for x in set_2 if element == x]
    return tmp
