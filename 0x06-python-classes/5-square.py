#!/usr/bin/python3
"""Printing a square"""


class Square:
    """ Private instance attribute: size

    property def size(self): to retrieve it
    property setter def size(self, value): to set it
    size must be an integer, otherwise raise a TypeError
    size is less than 0, raise a ValueError
    def area(self): that returns the current square area
    def my_print(self): that prints in stdout the square with the character #
    if size is equal to 0, print an empty line

    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

        def area(self):
            return self.__size ** 2

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            elif isinstance(value, int):
                self.__size = value

        def my_print(self):
            if self.__size != 0:
                for i in range(self.__size):
                    for j in range(self.__size):
                        print("#", end="")
                    print()
            else:
                print()
