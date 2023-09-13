#!/usr/bin/python3
"""Fucntion Declaration of   Pascal'Triangle """


def pascal_triangle(n):
    """Fucntion Body."""
    if n <= 0:
        return []

    trngs = [[1]]
    while len(trngs) != n:
        t = trngs[-1]
        tmps = [1]
        for j in range(len(t) - 1):
            tmps.append(t[j] + t[j + 1])
        tmps.append(1)
        trngs.append(tmps)
    return trngs
