#!/usr/bin/python3
"""Area of a square"""


class Square:
    """ Private instance attribute: size

    size must be an integer, otherwise raise a TypeError
    size is less than 0, raise a ValueError
    Area equal to self.__size **2

    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
