#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

from requests import get

if __name__ == "__main__":
    res = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
