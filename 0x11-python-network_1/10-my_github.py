#!/usr/bin/python3
"""Sends a search request to the Star Wars API"""
import requests
import sys

if __name__ == "__main__":
    search = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    r = requests.get(search)
    json_o = r.json()
    print("Number of results: {}".format(json_o.get('count')))
    for character in json_o.get('results'):
        print(character.get('name'))
