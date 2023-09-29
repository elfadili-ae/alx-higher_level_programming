#!/usr/bin/python3
"""Display the value of X-Request-Id."""
import urllib.request
import sys


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(dict(response.headers)["X-Request-Id"])
