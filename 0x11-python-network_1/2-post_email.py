#!/usr/bin/python3
"""with an URL and an email as argument sends a POST request
to the passed URL with the email as a parameter displaying the
body's response"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    data_encdd = parse.urlencode({'email': argv[2]}).encode()
    with request.urlopen(argv[1], data_encdd) as res:
        print(res.read().decode('utf-8'))
