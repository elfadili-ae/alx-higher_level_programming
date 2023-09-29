#!/usr/bin/python3
"""Display the value of X-Request-Id."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    resp = requests.get(url)
    print(resp.headers.get("X-Request-Id"))
