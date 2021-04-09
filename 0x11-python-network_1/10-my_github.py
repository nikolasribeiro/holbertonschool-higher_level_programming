#!/usr/bin/python3


""" Module 10-my_github"""
from sys import argv
from requests.auth import HTTPBasicAuth
import requests

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    resp = requests.get(
        "https://api.github.com/user", auth=HTTPBasicAuth(username, password)
    )
    json = resp.json()
    print(json.get("id"))
