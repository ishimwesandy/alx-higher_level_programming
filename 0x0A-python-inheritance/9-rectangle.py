#!/usr/bin/python3
"""Declaring Rectangle class  that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle using BaseGeometry. """

    def __init__(self, width, height):
        """Intialize """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return  area of  rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returning the  representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
