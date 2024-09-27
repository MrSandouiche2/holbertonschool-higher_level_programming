#!/usr/bin/python3
"""Module for Square class inheriting from Rectangle."""

class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes width and height, validating them as positive integers."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes the size of the square, validating it as a positive integer."""
        self.integer_validator("size", size)
        self.__size = size
        # Call the parent class's __init__ method with the same size for width and height
        super().__init__(size, size)

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
