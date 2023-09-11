#!/usr/bin/python3
""" Declaring   Rectangle class that inherits from BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """ Intialize. """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
