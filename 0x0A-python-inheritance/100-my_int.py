#!/usr/bin/python3
"""Declaring MyInt class  that inherits from int."""


class MyInt(int):
    """ operators == and !=."""

    def __eq__(self, value):
        """Override the opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override the  operator with == behavior."""
        return self.real == value
