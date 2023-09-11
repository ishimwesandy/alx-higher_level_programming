#!/usr/bin/python3
"""Declaring function that adds attribute to objects."""


def add_attribute(obj, att, value):
    """Add  attribute to an object if possible. """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
