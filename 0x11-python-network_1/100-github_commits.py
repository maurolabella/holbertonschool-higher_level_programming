#!/usr/bin/python3
"""Write a Python script that takes 2 arguments
in order to list 10 commits of the repository
'rails' by the user 'rails' """

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    commits_json = requests.get(url).json()
    count = 0
    for commit in commits_json:
        count += 1
        name = commit.get("commit").get("author").get("name")
        sha = commit.get("sha")
        print("{}:{}".format(sha, name))
        """ print(commit)"""
        if count == 1:
            break
