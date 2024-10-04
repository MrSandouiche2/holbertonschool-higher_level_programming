#!/usr/bin/env python3
"""le depart"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """Initialise l'objet."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """affiche attribut"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """sérialise"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to {filename}")
        except Exception as e:
            print(f"Failed to serialize object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """désérialise"""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Failed to deserialize object: {e}")
            return None
