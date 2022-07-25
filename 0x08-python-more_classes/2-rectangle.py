#!/usr/bin/python3
"""2-rectangle module
Class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

"""


class Rectangle:
    """Class Rectangle that defines a rectangle by
    : (based on 1-rectangle.py)
    """
    def __init__(self, width=0, height=0):
        """ Initialize instances"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get height"""
        return self.__height

    @height.sette
    def height(self, value):
        """ Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the Rectangle Area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Return the Rectangle Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
