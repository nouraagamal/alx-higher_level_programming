#!/usr/bin/python3
'''comment'''


def write_file(filename="", text=""):
    ''' writes string to text file UTF8 returns # of characters written'''
    with open(filename, mode='w', encoding='utf-8') as p:
        return p.write(text)
