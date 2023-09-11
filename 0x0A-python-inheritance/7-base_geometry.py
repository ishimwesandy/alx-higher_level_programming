#!/usr/bin/python3
"""Declaring  base geometry class BaseGeometry."""


class BaseGeometry:
    """Base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validated parameter . nt): The parameter to validate. """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
