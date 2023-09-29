#!/usr/bin/python3
"""Display the value of X-Request-Id."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    resp = requests.get(url)
    if resp.status_code == 200:
        print(resp.text)
    elif resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
