#!/usr/bin/python3
"""Search for a user using a letter."""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) == 2:
        vals = {"q": sys.argv[1]}
    else:
        vals = {"q": ""}

    resp = requests.post(url, data=vals)
    try:
        json = resp.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json["id"], json["name"]))
    except ValueError:
        print("Not a valid JSON")
