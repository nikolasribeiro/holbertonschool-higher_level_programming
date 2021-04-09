#!/bin/bash
# Bash script that takes in a URL, sends a POST to passed URL, displays body of response
curl -sd "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" $1
