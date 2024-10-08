#!/usr/bin/python3
"""

    Raises:
        TypeError: _description_
        ValueError: _description_
        TypeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """


class Rectangle:
    """Class that defines a rectangle by width and height, tracks instances."""

    # Public class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width ensuring it is an integer and >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height ensuring it is an integer and >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle.

        If either width or height is 0, perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the rectangle represented by the character '#'.

        If width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect_lines = ["#" * self.width for _ in range(self.height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Returns a string representation of the rectangle that can
        recreate the instance.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when the rectangle is deleted and decrements
        the instance count.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
