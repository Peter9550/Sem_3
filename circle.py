from .abstract_figure import GeometricFigure
from .color import FigureColor
import math


class Circle(GeometricFigure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    @property
    def figure_type(self):
        return self.FIGURE_TYPE

    def __repr__(self):
        return '{} {} цвета радиусом {}. Площадь = {:.2f}.'.format(
            self.figure_type,
            self.color,
            self.radius,
            self.area()
        )
