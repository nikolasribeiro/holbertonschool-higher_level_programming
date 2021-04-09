#!/usr/bin/python3


""" Module 6-post_email"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    payload = {"email": argv[2]}
    req = requests.post(url, data=payload)
    print(req.text)
