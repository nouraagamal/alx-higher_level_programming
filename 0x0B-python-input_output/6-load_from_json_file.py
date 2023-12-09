#!/usr/bin/python3
'''task 5 module'''


import json


def load_from_json_file(filename):
    '''creates an Object from a “JSON file”'''
    with open(filename, mode='r', encoding='utf-8') as p:
        return json.load(p)
