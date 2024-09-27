#!/usr/bin/python3
"""le depart"""


def inherits_from(obj, a_class):
    """return true si c'est une instance ou un class """
    return isinstance(obj, a_class) and type(obj) is not a_class
