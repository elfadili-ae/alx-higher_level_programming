#!/usr/bin/python3
"""Display the value of X-Request-Id."""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    vals = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(vals)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
