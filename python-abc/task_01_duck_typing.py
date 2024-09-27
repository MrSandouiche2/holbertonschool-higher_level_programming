from abc import ABC, abstractmethod
import math

# Classe abstraite Shape
class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

# Classe concrète Circle
class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

# Classe concrète Rectangle
class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

# Fonction shape_info
def shape_info(shape):
    """Print the area and perimeter of a shape, using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Test avec un cercle et un rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Info:")
shape_info(circle)  # Affichera l'aire et le périmètre du cercle

print("\nRectangle Info:")
shape_info(rectangle)  # Affichera l'aire et le périmètre du rectangle
