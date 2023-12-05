#!/bin/bash
# This Bash script accepts a URL as the first argument, sends a GET request to the URL with a custom header, and outputs the body of the response.
curl -sH "X-School-User-Id: 98" "${1}"
