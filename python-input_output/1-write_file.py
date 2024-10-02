#!/usr/bin/python3
"""le debut"""


def write_file(filename="", text=""):
    """va return le nombre de characteres"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
