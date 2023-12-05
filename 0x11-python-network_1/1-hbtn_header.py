#!/usr/bin/python3
"""Fetches URL, sends request, displays X-Request-Id in header"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
