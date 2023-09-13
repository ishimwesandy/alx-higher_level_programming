#!/usr/bin/python3
"""Declaring  function tha append ."""


def append_after(filename="", search_string="", new_string=""):
    """File Name in read mode and write mode"""
    text = ""
    with open(filename) as rd:
        for ln in rd:
            text += ln
            if search_string in ln:
                text += new_string
    with open(filename, "w") as wt:
        wt.write(text)
