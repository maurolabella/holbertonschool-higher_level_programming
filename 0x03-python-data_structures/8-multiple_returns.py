#!/usr/bin/python3

def multiple_returns(sentence):

    # if len(sentence):
    #     return(len(sentence), sentence[0])
    # return(0, None)
    length = len(sentence)
    if not(sentence and sentence.strip()):
        first = None
    else:
        first = sentence[0]
    res = (length, first)
    return(res)
