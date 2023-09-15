"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.
"""
import json


class FactorialException(Exception):
    def __init__(self, number: int):
        self.number = number

    def __str__(self):
        return f'Не существует факториал числа {self.number}'


class Factorial:

    def __init__(self, size: int):
        if size >= 0 and type(size) == int:
            self._size = size
        else:
            raise FactorialException(size)
        self.__base = []

    def history(self):
        return self.__base

    def __call__(self, n: int):
        res = 1
        for i in range(1, n + 1):
            res *= i

        if len(self.__base) >= self._size:
            self.__base.pop(0)
        self.__base.append({n: res})
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('base.json', 'w', encoding='UTF-8') as file:
            json.dump(self.__base, file)


if __name__ == '__main__':
    f1 = Factorial(size=-3)

