This repository contains Bash scripts and a Python function developed as part of the Alx Higher Level Programming curriculum.

## Task 0: cURL body size

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response. The size must be displayed in bytes. You have to use curl. Please test your script in the sandbox provided, using the web server running on port 5000.

Example:
```bash
./0-body_size.sh 0.0.0.0:5000
# Output: 10

./1-body.sh 0.0.0.0:5000/route_1
# Output: Route 2

./2-delete.sh 0.0.0.0:5000/route_3
# Output: I'm a DELETE request

./3-methods.sh 0.0.0.0:5000/route_4
# Output: OPTIONS, HEAD, PUT

./4-header.sh 0.0.0.0:5000/route_5
# Output: Hello School!

./5-post_params.sh 0.0.0.0:5000/route_6
# Output: POST params: email: test@gmail.com, subject: I will always be here for PLD

./6-main.py
