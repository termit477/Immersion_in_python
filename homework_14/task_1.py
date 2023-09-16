"""
Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
2-5 тестов на задание в трёх вариантах:
- doctest,
- unittest,
- pytest.
"""
import doctest


class TriangleException(Exception):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со стронами {self.a}, {self.b} и {self.c} невозможен. Повторите попытку.'


def checking_the_triangle(first_side: int, second_side: int, third_side: int):
    """Проверяет треугольник на равнобедренный, равносторонний, разносторонний или сообщает,
     что такого треугольника не может существовать.
    >>> checking_the_triangle(19, 19, 20)
    'Треугольник со сторонами a:19, b:19, c:20 - равнобедренный'

    >>> checking_the_triangle(10, 10, 10)
    'Треугольник со сторонами a:10, b:10, c:10 - равносторонний'

    >>> checking_the_triangle(15, 14, 13)
    'Треугольник со сторонами a:15, b:14, c:13 - разносторонний'
     """
    if first_side > second_side + third_side or \
            second_side > first_side + third_side or \
            third_side > first_side + second_side:
        raise TriangleException(first_side, second_side, third_side)
    elif first_side == second_side == third_side:
        return f'Треугольник со сторонами a:{first_side}, b:{second_side}, c:{third_side} - равносторонний'
    elif first_side == second_side or first_side == third_side or second_side == third_side:
        return f'Треугольник со сторонами a:{first_side}, b:{second_side}, c:{third_side} - равнобедренный'
    else:
        return f'Треугольник со сторонами a:{first_side}, b:{second_side}, c:{third_side} - разносторонний'


if __name__ == '__main__':
    doctest.main()
