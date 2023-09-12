#!/usr/bin/python3
"""Declaring Student Class."""


class Student:
    """Constraction initialization of Student Class."""

    def __init__(self, first_name, last_name, age):
        """new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Representation of the Student."""
        return self.__dict__
