"""This module provides a Circle class"""

import math

from Shape.shape import Shape


class Circle(Shape):
    """A circle in a 2D space"""

    def __init__(self, radius):
        super().__init__()
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def compute_area(self):
        return math.pi * self.radius**2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius
