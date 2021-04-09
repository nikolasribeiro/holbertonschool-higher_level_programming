#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first arg, displays body
curl -sI $1 | grep 'Allow' | cut -d':' -f2 | sed 's/^ *//'| tail -n +1
