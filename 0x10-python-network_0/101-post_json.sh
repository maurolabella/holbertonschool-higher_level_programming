#!/bin/bash
# scrip that POST "send" a JSON 
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
