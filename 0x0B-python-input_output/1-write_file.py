#!/usr/bin/python3
""" Fuction Declaration Body. """


def write_file(filename="", text=""):
    """Convert  a string to a UTF8 text file. in write mode """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
