#!/usr/bin/python3
"""depart"""


class Student:
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """initialisation"""
        if attrs is not None and isinstance(attrs, list):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
        else:
            return self.__dict__
