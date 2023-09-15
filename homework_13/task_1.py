"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.
"""


class TriangleException(Exception):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со стронами {self.a}, {self.b} и {self.c} невозможен. Повторите попытку.'


def checking_the_triangle(first_side: int, second_side: int, third_side: int):
    if first_side > second_side + third_side or \
            second_side > first_side + third_side or \
            third_side > first_side + second_side:
        raise TriangleException(first_side, second_side, third_side)
    elif first_side == second_side == third_side:
        print(f'Треугольник со сторонами a:{first_side}, b:{second_side}, c:{third_side} - равносторонний')
    elif first_side == second_side or first_side == third_side or second_side == third_side:
        print(f'Треугольник со сторонами a:{first_side}, b:{second_side}, c:{third_side} - равнобедренный')
    else:
        print(f'Треугольник со сторонами a:{first_side}, b:{second_side}, c:{third_side} - разносторонний')


if __name__ == '__main__':
    checking_the_triangle(19, 19, 20)
    checking_the_triangle(10, 10, 10)
    checking_the_triangle(15, 14, 13)
    checking_the_triangle(1, 15, 3)
