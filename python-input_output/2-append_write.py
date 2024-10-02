#!/usr/bin/python3
"""le depart"""

def append_write(filename="", text=""):
    """ la fonction"""
    with open(filename, 'a', encoding='utf-8') as f:
        nb_characters = f.write(text)
    return nb_characters
