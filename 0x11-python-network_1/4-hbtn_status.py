#!/usr/bin/python3
"""Fetch Alx intranet sattus."""
import requests


resp = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(resp.text)))
print("\t- content: {}".format(resp.text))
"""print("\t- content: {}".format(resp.content.decode('utf-8')))"""
