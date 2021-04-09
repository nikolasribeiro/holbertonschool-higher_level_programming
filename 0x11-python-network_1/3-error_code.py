#!/usr/bin/python3


""" Module 3-error_code"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode("utf8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
