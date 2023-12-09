#!/usr/bin/python3
'''comment'''


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

try:
    olddata = load_from_json_file('add_item.json')
except Exception:
    olddata = []

olddata.extend(arglist)
save_to_json_file(olddata, 'add_item.json')
