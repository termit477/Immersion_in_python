"""
Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
2-5 тестов на задание в трёх вариантах:
- doctest,
- unittest,
- pytest.
"""
import doctest


class FactorialException(Exception):
    def __init__(self, number: int):
        self.number = number

    def __str__(self):
        return f'Не существует факториал числа {self.number}'


class Factorial:
    """Функция высчитывает факториал положительного числа.

    >>> print(Factorial(5))
    120

    >>> print(Factorial(7))
    5040

    >>> print(Factorial(10))
    3628800
    """

    def __init__(self, size: int):
        if size >= 0 and type(size) == int:
            self._size = size
        else:
            raise FactorialException(size)

    def result(self):
        res = 1
        for i in range(1, self._size + 1):
            res *= i
        return res

    def __str__(self):
        return f'{self.result()}'


if __name__ == '__main__':
    doctest.main()
