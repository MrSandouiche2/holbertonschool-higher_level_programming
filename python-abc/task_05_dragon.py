class SwimMixin:
    """Mixin qui ajoute la capacité de nager."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin qui ajoute la capacité de voler."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """La classe Dragon qui hérite des capacités de nager et voler."""
    def roar(self):
        print("The dragon roars!")


# Assure-toi que cette section n'est exécutée qu'une seule fois
if __name__ == "__main__":
    draco = Dragon()
    draco.swim()   # The creature swims!
    draco.fly()    # The creature flies!
    draco.roar()   # The dragon roars!
