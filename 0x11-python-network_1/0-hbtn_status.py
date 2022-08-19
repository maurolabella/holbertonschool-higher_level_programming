#!/usr/bin/python3
"""
write a script that fetches https://intranet.hbtn.io/status
"""

from urllib import request


def main():
    """ main executable"""
    with request.urlopen("https://intranet.hbtn.io/status") as webf_fetch:
        res = webf_fetch.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print(f"\t- content: {res}")
        print(f"\t- utf8 content: {res.decode('utf-8')}")


if __name__ == "__main__":
    """instruction to not executes when imported"""
    main()
