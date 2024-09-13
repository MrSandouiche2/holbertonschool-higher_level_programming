#!/usr/bin/python3

def uniq_add(my_list=[]):
    resu = 0
    my_set = set(my_list)
    for item in my_set:
        resu += item
    return resu
