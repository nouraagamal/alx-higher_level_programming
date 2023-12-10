#!/usr/bin/python3
'''comment'''


class Base:
    '''a base class for other classes'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialization of a Base instance'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
