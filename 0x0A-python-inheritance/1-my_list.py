#!/usr/bin/python3
"""Defines list class MyList."""


class MyList(list):
    """Built-in list class that do Sort."""

    def print_sorted(self):
        """Print a  sorted list in ascending order."""
        print(sorted(self))

