#!/usr/bin/python3
"""Base of the whole program"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
