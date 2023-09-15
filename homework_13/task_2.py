"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.
"""


class RectangleException(Exception):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def __str__(self):
        return f'Прямоугольник со сторонами {self.length} и {self.width} невозможен. Повторите попытку.'


class Rectangle:

    def __init__(self, length: float, width: float = None):
        if length > 0 and width > 0:
            self.length = length
            if width:
                self.width = width
            else:
                self.width = length
        else:
            raise RectangleException(length, width)

    def calc_len(self):
        return (self.width + self.length) * 2

    def calc_area(self):
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(self.length + other.length, self.width + other.width)

    def __sub__(self, other):
        return Rectangle(self.length - other.length, self.width - other.width)

    def __eq__(self, other):
        return self.calc_area() == other.calc_area()

    def __lt__(self, other):
        return self.calc_area() < other.calc_area()

    def __gt__(self, other):
        return self.calc_area() > other.calc_area()

    def __le__(self, other):
        return self.calc_area() <= other.calc_area()

    def __ge__(self, other):
        return self.calc_area() >= other.calc_area()


if __name__ == '__main__':
    prim1 = Rectangle(length=-2, width=2)
    prim2 = Rectangle(length=5, width=4)
