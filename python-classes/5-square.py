#!/usr/bin/python3
"""Module for defining a Square class."""


class Square:
    """Represents a square shape."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters."""
        if self.size == 0:
            print("")
            return
        for i in range(self.size):
            print("#" * self.size)
