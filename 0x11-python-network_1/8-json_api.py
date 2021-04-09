#!/usr/bin/python3


""" Module 8-json_api"""
from sys import argv
import requests


if __name__ == "__main__":
    try:
        payload = {"q": argv[1]}
    except:
        payload = {"q": ""}

    resp = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    if resp.headers["Content-type"] == "application/json":
        json = resp.json()
        if len(json) != 0:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
