# This repository contains Bash scripts and a Python function developed as part of the Alx Higher Level Programming curriculum.

## Task 0: cURL body size

Example:
```bash
./0-body_size.sh 0.0.0.0:5000
# Output: 10

Task 1: cURL to the end
./1-body.sh 0.0.0.0:5000/route_1
# Output: Route 2

Task 2: cURL Method
./2-delete.sh 0.0.0.0:5000/route_3
# Output: I'm a DELETE request

Task 3: cURL only methods
./3-methods.sh 0.0.0.0:5000/route_4
# Output: OPTIONS, HEAD, PUT

Task 4: cURL headers
./4-header.sh 0.0.0.0:5000/route_5
# Output: Hello School!

Task 5: cURL POST parameters
./5-post_params.sh 0.0.0.0:5000/route_6
# Output: POST params: email: test@gmail.com, subject: I will always be here for PLD

Task 6: Find a peak
./6-main.py

Task 7: Only status code
./100-status_code.sh 0.0.0.0:5000
# Output: 200
./100-status_code.sh 0.0.0.0:5000/nop
# Output: 404

Task 8: cURL a JSON file
./101-post_json.sh 0.0.0.0:5000/route_json my_json_0
# Output: Valid JSON
./101-post_json.sh 0.0.0.0:5000/route_json my_json_1
# Output: Not a valid JSON
./101-post_json.sh 0.0.0.0:5000/route_json my_json_2
# Output: Not a valid JSON

Task 9: Catch me if you can!
./102-catch_me.sh
# Output: You got me!
