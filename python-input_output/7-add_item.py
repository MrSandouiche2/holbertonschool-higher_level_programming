#!/usr/bin/python3
"""le depart"""


import sys
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"

arg = sys.argv[1:]


def name():
    """placeholder"""
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []
    items.extend(arg)
    save_to_json_file(items, filename)
