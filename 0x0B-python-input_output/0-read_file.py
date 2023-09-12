#!/usr/bin/python3
"""Declaring  function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Print the contents  on the user screen"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
