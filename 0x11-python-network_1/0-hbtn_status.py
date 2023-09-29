#!/usr/bin/python3
"""Fetch Alx intranet sattus."""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("    - type: ", end="")
    print(type(html))
    print("    - content: ", end="")
    print(html)
    print("    - utf8 content: ", end="")
    print(html.decode('utf8'))
