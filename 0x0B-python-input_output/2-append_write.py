#!/usr/bin/python3
"""Fuction Declaration Body of appending file ."""


def append_write(filename="", text=""):
    """Appends a character. """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
