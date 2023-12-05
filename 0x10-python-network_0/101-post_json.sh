#!/bin/bash
# Sends JSON POST request to URL, shows response body
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
