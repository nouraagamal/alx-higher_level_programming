#!/usr/bin/python3
'''comment'''


class MyList(list):
    '''prints the list, but sorted (ascending sort)'''
    def print_sorted(self):
        '''method to print sorted list'''
        print(sorted(self))
