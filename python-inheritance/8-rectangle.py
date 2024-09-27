#!/usr/bin/python3
"""le depart"""


class BaseGeometry:
    """la classe """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Classe Rectangle qui hérite de BaseGeometry"""

    def __init__(self, width, height):
        """Initialise le rectangle avec largeur et hauteur validées"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
