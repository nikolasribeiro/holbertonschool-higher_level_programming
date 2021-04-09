#!/bin/bash
# Bash script that sends a request to a URL passed as an arg, displays status code only
curl -w "%{http_code}" -s -o /dev/null "$1"
