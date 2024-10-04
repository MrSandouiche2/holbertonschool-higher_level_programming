#!/usr/bin/python3
"""depart"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initialisation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """fonction"""
        return self.__dict__
