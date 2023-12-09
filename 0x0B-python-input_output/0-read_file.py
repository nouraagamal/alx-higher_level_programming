#!/usr/bin/python3
'''comment'''


def read_file(filename=""):
    '''reads a file in utf-8 encoding'''
    with open(filename, encoding='utf-8') as p:
        print(p.read(), end='')
