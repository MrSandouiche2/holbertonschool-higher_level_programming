#!/usr/bin/env python3
"""le depart"""

import json


def serialize_and_save_to_file(data, filename):
    """ initialisation"""

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)
    print(f"Data serialized and saved to '{filename}'.")


def load_and_deserialize(filename):
    """ initialisation"""

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
