#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    i = sorted(a_dictionary)

    for key in i:
        print(f"{key}: {a_dictionary[key]}")
