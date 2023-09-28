#!/bin/bash
# send a request to the URL and print the body response
curl -sI "$1" | grep "Allow" | cut -d" " -f 2-
