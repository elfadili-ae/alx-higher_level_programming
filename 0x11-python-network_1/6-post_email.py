#!/usr/bin/python3
"""Display the value of X-Request-Id."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    vals = {"email": sys.argv[2]}

    resp = requests.post(url, data=vals)
    print(resp.text)
