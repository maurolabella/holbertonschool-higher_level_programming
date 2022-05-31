#!/usr/bin/python3
"""Tasks: Load, add, save"""

import os.path
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]
list = []
file_name = "add_item.json"

if os.path.exists(file_name):
    list = load_from_json_file(file_name)

save_to_json_file(list + arguments, file_name)
