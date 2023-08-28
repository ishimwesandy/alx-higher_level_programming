#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = a_dictionary.copy()
    listofkey = list(nd.keys())
    for j in listofkey:
        nd[j] *= 2
    return (nd)
