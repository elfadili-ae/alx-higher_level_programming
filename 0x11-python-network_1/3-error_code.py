#!/usr/bin/python3
"""Display the value of X-Request-Id."""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = urllib.request.urlopen(url)
        body = response.read()
        print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
