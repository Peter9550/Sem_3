from .abstract_figure import GeometricFigure
from .color import FigureColor


class Rectangle(GeometricFigure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    @property
    def figure_type(self):
        return self.FIGURE_TYPE

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {}. Площадь = {:.2f}.'.format(
            self.figure_type,
            self.color,
            self.width,
            self.height,
            self.area()
        )
