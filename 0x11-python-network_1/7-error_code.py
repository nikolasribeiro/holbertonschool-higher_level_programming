#!/usr/bin/python3


""" Module 7-error_code"""
from sys import argv
import requests

if __name__ == "__main__":
    url = requests.get(argv[1])
    if url.status_code >= 400:
        print("Error code: {}".format(url.status_code))
    else:
        print(url.text)
