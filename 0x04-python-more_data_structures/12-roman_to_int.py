#!/usr/bin/python3


def roman_to_int(roman_string):

    if not(isinstance(roman_string, str)) or roman_string is None:
        return None
    romans = ["M", "D", "C", "L", "X", "V", "I"]
    decimals = [1000, 500, 100, 50, 10, 5, 1]
    base = list(roman_string)
    bse_x = [int(decimals[romans.index(elem)]) for elem in roman_string]
    max = bse_x[-1]
    sum = 0
    for i in reversed(range(len(bse_x))):
        if bse_x[i] < max:
            sum = sum - bse_x[i]
        else:
            max = bse_x[i]
            sum = sum + bse_x[i]
    return sum

# bse_sum = [(lambda x: x if (x >= max) else -x)
#            for x in bse_x]
