#!/usr/bin/python3
'''comment'''


def append_write(filename="", text=""):
    '''appends a string at the end of a text file'''
    with open(filename, mode='a', encoding='utf-8') as p:
        return p.write(text)
