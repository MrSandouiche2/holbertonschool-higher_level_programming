#!/usr/bin/python3
"""Module for defining a Square class."""


class Square:
    """Represents a square shape with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position.

        Args:
            size (int): The size of the square, must be >= 0.
            position (tuple): The position of the square, must be a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, ensuring it's an integer >= 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, ensuring it's a tuple of 2 positive integers."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # at the given position."""
        if self.__size == 0:
            print("")
            return
        [print("") for _ in range(self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

