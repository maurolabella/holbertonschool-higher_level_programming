#!/usr/bin/python3

from http.client import SWITCHING_PROTOCOLS
from sys import setswitchinterval
from unittest import case


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        new_element = 0
        try:
            new_element = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("{}".format("division by 0"))
        except IndexError:
            print("{}".format("out of range"))
        except TypeError:
            print("{}".format("wrong type"))
        finally:
            new_list.append(new_element)
    return new_list
