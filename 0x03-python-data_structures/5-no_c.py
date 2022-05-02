#!/usr/bin/python3

def no_c(my_string):
    for character in "cC":
        new_string = my_string.replace(character, "")
    return(new_string)
