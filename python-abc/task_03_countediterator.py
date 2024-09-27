class CountedIterator:
    """An iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Obtenir l'itérateur à partir de l'itérable
        self.count = 0  # Initialiser le compteur

    def __next__(self):
        try:
            item = next(self.iterator)  # Appeler la méthode `next` de l'itérateur original
            self.count += 1  # Incrémenter le compteur à chaque appel
            return item  # Retourner l'élément suivant
        except StopIteration:
            raise StopIteration  # Réélever l'exception StopIteration si l'itérateur est épuisé

    def get_count(self):
        """Retourner le nombre d'éléments itérés."""
        return self.count

    def __iter__(self):
        """Renvoyer l'objet lui-même comme itérateur."""
        return self

# Exemple d'utilisation
items = [10, 20, 30, 40]

# Créer un itérateur compté
counted_iter = CountedIterator(items)

# Itérer sur les éléments et afficher leur nombre
for item in counted_iter:
    print(f"Item: {item}, Count: {counted_iter.get_count()}")

# Vérifier le nombre total d'éléments itérés
print(f"Total items iterated: {counted_iter.get_count()}")
