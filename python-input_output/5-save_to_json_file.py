#!/usr/bin/python3
"""starter"""

import json


def save_to_json_file(my_obj, filename):
    """la fonction principal"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
