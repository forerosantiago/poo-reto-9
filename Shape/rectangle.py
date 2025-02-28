"""Rectangle class"""

from Shape.shape import Shape
from Shape.shape import timeFunction

class Rectangle(Shape):
    """A rectangle in a 2D space"""

    def __init__(self, width, height):
        super().__init__()
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @timeFunction
    def compute_area(self) -> float:
        return self.width * self.height

    @timeFunction
    def compute_perimeter(self) -> float:
        return 2 * (self.width + self.height)
