#!/bin/bash
#retrieves the method that a server allows
curl -sI -X OPTIONS localhost | grep Allow | cut -d' ' -f2 -
