# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
from random import randint


def sum_fractions(a: Fraction, b: Fraction) -> Fraction:
    return a + b


def multiply_fractions(a: Fraction, b: Fraction) -> Fraction:
    return a * b


run = True
while run:
    input_number = input(
        'Нажмите "ENTER", чтобы сгенерировать дроби или введите что угодно, чтобы выйти из программы: ')
    if input_number == '':
        a = Fraction(randint(1, 50), randint(1, 50))
        b = Fraction(randint(1, 50), randint(1, 50))
        print(f'Первая дробь: {a}')
        print(f'Вторая дробь: {b}')
        print((f'Сумма дробей: {sum_fractions(a, b)}'))
        print((f'Произведение дробей: {multiply_fractions(a, b)}'))
        print('----------------------------------')
    else:
        print('Программа завершена.')
        run = False