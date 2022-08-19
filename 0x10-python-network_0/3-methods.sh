#!/bin/bash
#retrieves the method that a server allows
curl -sI -X OPTIONS "$1" | grep Allow: | cut -d' ' -f2-
