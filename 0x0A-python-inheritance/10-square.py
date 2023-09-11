#!/usr/bin/python3
"""Declaring a Rectangle subclass Square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing of square."""

    def __init__(self, size):
        """Initialize """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
