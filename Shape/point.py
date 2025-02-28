"""This module contains the Point class"""

import math


class Point:
    """A point in a 2D space"""

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, value: float):
        self._y = value

    def compute_distance(self, other_point: "Point") -> float:
        """Compute the distance between two points"""
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
