#!/usr/bin/python3
"""Class Declaration of Student """


class Student:
    """Student Constructor ."""

    def __init__(self, first_name, last_name, age):
        """ New Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Student """
        if (type(attrs) == list and
                all(type(elemet) == str for elemet in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes of the Student."""
        for j, value in json.items():
            setattr(self, j, value)
