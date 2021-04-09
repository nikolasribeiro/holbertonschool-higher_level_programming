#!/usr/bin/python3


""" Module 1-hbtn_header"""
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        html = response.getheader("X-Request-Id")
    print(html)
