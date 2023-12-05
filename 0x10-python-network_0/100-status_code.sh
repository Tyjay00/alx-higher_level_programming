   #!/bin/bash
# Sends request to URL, shows status code
curl -so /dev/null -w "%{http_code}" "$1"
