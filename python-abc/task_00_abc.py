from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented in derived classes."""
        pass


class Dog(Animal):
    """Dog class, subclass of Animal."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class, subclass of Animal."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"


# Example of usage
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
