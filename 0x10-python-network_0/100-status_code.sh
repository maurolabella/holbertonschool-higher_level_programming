#!/bin/bash
#write a Bash scripts to retrieve only the status code of the response
curl -s -L -I "$1" -o /dev/null -w '%{http_code}'
