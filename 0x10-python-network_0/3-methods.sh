#!/bin/bash
# This Bash script accepts a URL as the first argument, sends an OPTIONS request to the URL, and outputs the allowed methods for the resource.
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
