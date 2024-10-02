#!/usr/bin/python3
"""le depart"""

def append_write(filename="", text=""):
    with open(filename,'a', encoding='utf-8') as f:
        f.write(text)
