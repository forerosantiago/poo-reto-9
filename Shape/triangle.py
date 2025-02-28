"""A module for the Triangle class"""

from Shape.shape import Shape
from shape import timeFunction

class Triangle(Shape):
    """A triangle in a 2D space"""

    def __init__(self, side1, side2, side3):
        super().__init__()
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    @property
    def side1(self):
        return self._side1
    
    @side1.setter
    def side1(self, value):
        if value <= 0:
            raise ValueError("Side must be positive")
        self._side1 = value

    @property
    def side2(self):
        return self._side2
    
    @side2.setter
    def side2(self, value):
        if value <= 0:
            raise ValueError("Side must be positive")
        self._side2 = value

    @property
    def side3(self):
        return self._side3
    
    @side3.setter
    def side3(self, value):
        if value <= 0:
            raise ValueError("Side must be positive")
        self._side3 = value

    @timeFunction
    def compute_area(self):
        # Compute the area of the triangle using Heron's formula
        semiperimeter = self.compute_perimeter() / 2
        return (
            semiperimeter
            * (semiperimeter - self.side1)
            * (semiperimeter - self.side2)
            * (semiperimeter - self.side3)
        ) ** 0.5

    @timeFunction
    def compute_perimeter(self):
        return self.side1 + self.side2 + self.side3
