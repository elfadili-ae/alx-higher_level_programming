#!/bin/bash
# send a POST request to the URL
curl -s -X POST -H "Content-Type:applicatiOn/json" -d @"$2" "$1"
