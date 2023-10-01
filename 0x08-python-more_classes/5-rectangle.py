#!/usr/bin/python3
"""Declaring  Rectangle class"""


class Rectangle:
    """rectangle representation"""

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter and setter rectangle Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter rectangle Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area """
        return (self.__width * self.__height)

    def perimeter(self):
        """Return  perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for j in range(self.__height):
            [rec.append('#') for i in range(self.__width)]
            if j != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        print("Bye rectangle...")