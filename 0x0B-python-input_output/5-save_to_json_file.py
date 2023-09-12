#!/usr/bin/python3
"""Declararing  function Body"""
import json


def save_to_json_file(my_obj, filename):
    """Write  text file using JSON File."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
