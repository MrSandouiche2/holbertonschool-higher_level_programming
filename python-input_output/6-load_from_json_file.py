#!/usr/bin/python3
"""le depart du programme"""

import json
def load_from_json_file(filename):
    """creer objet json"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
