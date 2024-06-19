#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
