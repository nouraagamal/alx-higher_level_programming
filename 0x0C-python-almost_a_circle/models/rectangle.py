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

    def update(self, *args, **kwargs):
        """Updates attributes of an instance"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
