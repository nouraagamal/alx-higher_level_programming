#!/usr/bin/python3
'''comment'''


import json


def save_to_json_file(my_obj, filename):
    '''writes obj to file in json format'''
    with open(filename, mode='w', encoding='utf-8') as p:
        json.dump(my_obj, p)
