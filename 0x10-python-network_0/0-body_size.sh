#!/bin/bash
# This Bash script accepts a URL as input, sends a GET request to the URL, and outputs the size of the response body.
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
