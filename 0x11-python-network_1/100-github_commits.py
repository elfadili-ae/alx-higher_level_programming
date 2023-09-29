#!/usr/bin/python3
"""Get rails repo last 10 commits id and author."""

import requests
import sys


if __name__ == "__main__":
    username = "rails"
    repo = "rails"

    url = " https://api.github.com/repos/{}/{}/commits".format(username, repo)

    resp = requests.get(url)
    data = resp.json()
    for i in range(0, 10):
        committer = data[i].get("commit").get("author").get("name")
        print("{}: {}".format(data[i].get("sha"), committer))
