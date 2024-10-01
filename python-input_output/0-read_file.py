#!/usr/bin/python3
"""placeholder"""


def read_file(filename=""):
    """Reads a text file and prints its content to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
