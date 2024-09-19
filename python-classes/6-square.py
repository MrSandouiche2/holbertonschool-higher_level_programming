#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Represents a square shape."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a private size and position attribute.

        Args:
            size (int): The size of the square, must be >= 0.
            position (tuple): A tuple of 2 positive integers, the position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
