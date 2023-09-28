#!/bin/bash
# send a POST request to the URL
curl -s -X POST -d "emailtest@gmail.com" -d "subject=I will always be here for PLD" "$1"
