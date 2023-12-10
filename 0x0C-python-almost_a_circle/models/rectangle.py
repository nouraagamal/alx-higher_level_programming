#!/usr/bin/python3
'''comment'''


from models.base import Base


class Rectangle(Base):
    '''rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes a Rectangle instance'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Retrieves the width attribute'''
        return self.__width

    @property
    def height(self):
        '''Retrieves the height attribute'''
        return self.__height

    @property
    def x(self):
        '''Retrieves the x attribute'''
        return self.__x

    @property
    def y(self):
        '''Retrieves the y attribute'''
        return self.__y

    @width.setter
    def width(self, value):
        '''Sets the width attribute'''
        self.__width = value

    @height.setter
    def height(self, value):
        '''Sets the height attribute'''
        self.validate("height", value, False)
        self.__height = value

    @x.setter
    def x(self, value):
        '''Sets the x attribute'''
        self.validate("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        '''Sets y attribute'''
        self.validate("y", value)
        self.__y = value

    def validate(self, name, value, o=True):
        '''to validate values'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if o and value < 0:
            raise TypeError("{} must be >= 0".format(name))
        elif not o and value <= 0:
            raise TypeError("{} must be > 0".format(name))

    def area(self):
        '''calculates area of rectangle'''
        return self.width * self.height

    def display(self):
        '''Prints the Rectangle instance with the # character'''
        p = '\n' * self.y * \
                (' ' * self.x * '#' * self.width * '\n') * self.height
        print(p, end='')

    def __str__(self):
        '''"Returns a string representation of a Rectangle instance'''
        p = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return p
