#!/bin/bash
# Bash script that makes request to 0.0.0.0:5000/catch_me, server responds You got me!
curl -sLX PUT 0.0.0.0:5000/catch_me -d"user_id=98" -H "Origin: HolbertonSchool"
