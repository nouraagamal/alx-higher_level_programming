#!/usr/bin/python3
'''comment'''


class BaseGeometry:
    '''empty class'''
    def __init__(self):
        '''comment'''
        pass
    def area(self):
        '''function doesn't work'''
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        '''another not working function'''
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer'.format(name))
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0'.format(name))
