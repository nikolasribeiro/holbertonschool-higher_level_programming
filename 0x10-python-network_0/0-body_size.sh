#!/bin/bash
# Bash script that takes in a URL, sends request to URL, displays size
curl -sI $1 | grep 'Content-Length' | cut -d' ' -f2
