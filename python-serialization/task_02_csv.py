#!/usr/bin/env python3
"""depart"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """fonction"""
    try:

        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"Le fichier {csv_filename} n'a pas été trouvé.")
        return False
    except Exception as e:
        print(f"Erreur : {e}")
        return False
