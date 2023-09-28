#!/bin/bash
# send a request to the URL and display body response
curl -s -X "GET" -H "X-School-User-Id:98" "$1"
