#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""color_enum.py: enum for every color of the cube"""

__author__ = "Lucas Bulloni, Malik Fleury, Bastien Wermeille"
__version__ = "1.0.0"


from enum import Enum, auto

class Color(Enum):
    """
    color for the cube
    """
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()
    ORANGE = auto()
    WHITE = auto()
