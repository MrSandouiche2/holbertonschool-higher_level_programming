#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for i, element in enumerate(ligne):
            if i < len(ligne)-1:
                print("{}".format(element), end=" ")
            else:
                print("{}".format(element), end="")
        print()
