#!/bin/bash
# send a POST request to the URL
curl -s -w "%{http_code}" -o /dev/null "$1"
