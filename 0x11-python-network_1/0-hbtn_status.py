#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status")\
            as webf_fetch:
        res = webf_fetch.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print(f"\t- content: {res}")
        print(f"\t- utf8 content: {res.decode()}")
