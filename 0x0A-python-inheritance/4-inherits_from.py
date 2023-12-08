#!/usr/bin/python3
'''comment'''


def inherits_from(obj, a_class):
    '''returns True if the object is an instance of a class that inherited'''
    return type(obj) != a_class and issubclass(type(obj), a_class)
