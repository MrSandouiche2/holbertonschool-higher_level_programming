#!/usr/bin/python3
"""Module for defining a Square class."""


class Square:
    """Represents a square shape."""

    def __init__(self, size):
        """Initialize the square with a private size attribute.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private size attribute
