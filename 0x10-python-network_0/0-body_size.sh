#!/bin/bash
# a Bash script that takes in a URL and retrieves Content-Length
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
