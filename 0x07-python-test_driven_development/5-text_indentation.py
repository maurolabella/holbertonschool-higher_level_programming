#!/usr/bin/python3
"""
text_indentation - prints a text with 2 new lines after each of
these characters: .,? and :
The print follow some other whimsical requirements
"""


def text_indentation(txt):
    """
    @text: must be a string to avoid raise a TypeError exception with the message text must be a string
    """
    if isinstance(txt, (str)) is True:
        buffer = []
        long = len(txt) - 1
        for i, char in enumerate(txt):
            buffer.append(char)
            if char in ['.', '?', ':']:
                print("".join(buffer).strip())
                print("")
                buffer = []
            if(i == long):
                print("".join(buffer).strip(), end="")
    else:
        raise TypeError("text must be a string")
