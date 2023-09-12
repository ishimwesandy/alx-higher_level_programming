#!/usr/bin/python3
"""Declaring  class Body."""


def class_to_json(obj):
    """Return the dictionary description """
    return obj.__dict__
