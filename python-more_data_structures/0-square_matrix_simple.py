#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nouvelle_matrice = []

    for ligne in matrix:
        nouvelle_ligne = [element ** 2 for element in ligne]

        nouvelle_matrice.append(nouvelle_ligne)

    return nouvelle_matrice
