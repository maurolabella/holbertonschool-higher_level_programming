#!/usr/bin/python3
"""script that takes an url, sends a rquest and get X-Request_Id var"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as res:
        print(res.getheader("X-Request-Id"))
