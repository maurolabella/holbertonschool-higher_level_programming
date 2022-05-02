#!/usr/bin/python3

from tokenize import blank_re


def multiple_returns(sentence):
    length = len(sentence)
    if not(sentence and sentence.strip()):
        first = None
    else:
        first = sentence[0]
    res = (length, first)
    return(res)
