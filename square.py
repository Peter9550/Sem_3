from .rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    @property
    def figure_type(self):
        return self.FIGURE_TYPE

    def __repr__(self):
        return '{} {} цвета со стороной {}. Площадь = {:.2f}.'.format(
            self.figure_type,
            self.color,
            self.width,
            self.area()
        )
