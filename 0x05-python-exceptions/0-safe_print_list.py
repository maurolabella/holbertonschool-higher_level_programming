#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    items = 0
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            items += 1
        print("")
    except IndexError:
        print("")
    return (items)
