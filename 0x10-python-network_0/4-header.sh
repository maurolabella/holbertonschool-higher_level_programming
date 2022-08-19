#!/bin/bash
# sends a guest request with header variables
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
