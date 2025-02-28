"""Module defining the Line class"""

from shape import timeFunction
from point import Point

class Line:
    """A line in a 2D space"""

    def __init__(self, start_point: "Point", end_point: "Point"):
        self._start_point = start_point
        self._end_point = end_point
        self.length = self.compute_length()

    @property
    def start_point(self) -> "Point":
        return self._start_point
    
    @start_point.setter
    def start_point(self, value: "Point"):
        self._start_point = value
        self.length = self.compute_length()

    @property
    def end_point(self) -> "Point":
        return self._end_point
    
    @end_point.setter
    def end_point(self, value: "Point"):
        self._end_point = value
        self.length = self.compute_length()


    @timeFunction
    def compute_length(self) -> float:
        """Compute the length of the line"""
        return self.start_point.compute_distance(self.end_point)
