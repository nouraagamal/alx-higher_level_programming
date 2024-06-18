#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
displays the body of the response (decoded in utf-8).
manage urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
