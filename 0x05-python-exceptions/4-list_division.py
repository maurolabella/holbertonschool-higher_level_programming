#!/usr/bin/python3

from http.client import SWITCHING_PROTOCOLS
from sys import setswitchinterval
from unittest import case


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    new = 0
    for i in range(list_length):
        try:
            new_element = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            new = 0
            print("{}".format("division by 0"))
        except IndexError:
            new = 0
            print("{}".format("out of range"))
        except TypeError:
            new = 0
            print("{}".format("wrong type"))
        finally:
            new_list.append(new_element)
    return (new_list)
