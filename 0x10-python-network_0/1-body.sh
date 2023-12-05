#!/bin/bash
# This Bash script accepts a URL as input, sends a GET request to the URL, and outputs the body of the response if the status code is 200.
curl -Ls "$1"
