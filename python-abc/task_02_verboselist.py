# Définir la classe VerboseList qui hérite de list
class VerboseList(list):
    """A custom list that prints messages when items are added or removed."""

    # Surcharge de la méthode append
    def append(self, item):
        super().append(item)  # Appel de la méthode d'origine
        print(f"Added {item} to the list.")

    # Surcharge de la méthode extend
    def extend(self, iterable):
        length_before = len(self)
        super().extend(iterable)  # Appel de la méthode d'origine
        length_after = len(self)
        added_items = length_after - length_before
        print(f"Extended the list with {added_items} items.")

    # Surcharge de la méthode remove
    def remove(self, item):
        if item in self:
            print(f"Removed {item} from the list.")
        super().remove(item)  # Appel de la méthode d'origine

    # Surcharge de la méthode pop
    def pop(self, index=-1):
        popped_item = super().pop(index)  # Appel de la méthode d'origine
        print(f"Popped {popped_item} from the list.")
        return popped_item

# Test de la classe VerboseList
vlist = VerboseList([1, 2, 3])

# Test de la méthode append
vlist.append(4)
# Output attendu : Added 4 to the list.

# Test de la méthode extend
vlist.extend([5, 6, 7])
# Output attendu : Extended the list with 3 items.

# Test de la méthode remove
vlist.remove(2)
# Output attendu : Removed 2 from the list.

# Test de la méthode pop
vlist.pop()
# Output attendu : Popped 7 from the list.

vlist.pop(0)
# Output attendu : Popped 1 from the list.
