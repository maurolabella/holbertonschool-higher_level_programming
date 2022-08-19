#!/usr/bin/python3
"""display the response's body to a directed request"""

from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        code = str(e).split(' ')[2][:-1]
        print("Error code: " + str(code))
