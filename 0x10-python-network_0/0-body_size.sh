#!/usr/bin/bash
# send a request to the URL > usage: ./0-body_size.sh <url>

curl -sI $1 | grep "Content-Length" | cut -d" " -f 2
