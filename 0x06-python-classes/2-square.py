#!/usr/bin/python3
"""Size validation"""


class Square:
    """ Private instance attribute: size

    must be an integer, otherwise raise a TypeError
    if size is less than 0, raise a ValueError

    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
