#!/usr/bin/python3
"""Get github account ID"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]

    url = "https://api.github.com/users/" + username

    data = {"Authorization": "token {}".format(passwd)}

    resp = requests.get(url, headers=data)
    print(resp.json().get("id"))
