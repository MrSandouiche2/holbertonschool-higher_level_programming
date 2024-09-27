class Fish:
    def swim(self):
        print("The fish is swimming.")

    def habitat(self):
        print("The fish lives in water.")


class Bird:
    def fly(self):
        print("The bird is flying.")

    def habitat(self):
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    # Instancie le FlyingFish une seule fois
    flying_fish = FlyingFish()

    # Appelle les méthodes une seule fois
    flying_fish.swim()   # The flying fish is swimming!
    flying_fish.fly()    # The flying fish is soaring!
    flying_fish.habitat()  # The flying fish lives both in water and the sky!

    # Affiche la méthode de résolution d'ordre
    print(FlyingFish.mro())
