#!/usr/bin/python3
"""Get rails repo last 10 commits id and author."""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[2]
    repo = sys.argv[1]

    url = " https://api.github.com/repos/{}/{}/commits".format(username, repo)

    resp = requests.get(url)
    data = resp.json()
    try:
        for i in range(0, 10):
            committer = data[i].get("commit").get("author").get("name")
            print("{}: {}".format(data[i].get("sha"), committer))
    except IndexError:
        pass
