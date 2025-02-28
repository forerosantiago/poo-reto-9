"""This module defines the Shape class, the methods have a decorator that measures their execution time."""

import time

def timeFunction(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
    return wrapper

class Shape:
    """A generic shape in a 2D space"""

    shape_type = "Generic Shape" # default value

    def __init__(self):
        pass

    @timeFunction
    def compute_area(self) -> float:
        """Compute the area of the shape"""
        raise NotImplementedError("Subclasses should implement this method")

    @timeFunction
    def compute_perimeter(self) -> float:
        """Compute the perimeter of the shape"""
        raise NotImplementedError("Subclasses should implement this method")

    @classmethod
    def set_shape_type(cls, shape_type: str):
        """Set the type of the shape"""
        cls.shape_type = shape_type
