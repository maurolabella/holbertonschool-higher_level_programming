#!/usr/bin/python3
def uniq_add(my_list=[]):
    tmp = []
    sum = 0
    for element in my_list:
        if element not in tmp:
            tmp.append(element)
            sum = sum + element
    return sum
