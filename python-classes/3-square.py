#!/usr/bin/python3
"""Module for defining a Square class."""


class Square:
    """Represents a square shape."""

    def __init__(self, size=0):
        """Initialize the square with a private size attribute.

        Args:
            size (int): The size of the square, must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate and return the current area of the square.

        Returns:
            int: The area of the square, which is size squared.
        """

        return self.__size ** 2