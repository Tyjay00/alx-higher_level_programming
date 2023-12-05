#!/bin/bash
# This Bash script accepts a URL as the first argument, sends a DELETE request to the URL, and outputs the body of the response.
curl -s "$1" -X DELETE
