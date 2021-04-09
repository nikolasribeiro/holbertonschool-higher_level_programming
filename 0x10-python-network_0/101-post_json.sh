#!/bin/bash
# Bash script that takes in a URL, sends a POST to passed URL, displays body of response
curl -sX POST --header "Content-Type: application/json" "$1" -d @"$2"
