"""
Напишите следующие функции:

- Нахождение корней квадратного уравнения
- Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
- Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
- Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
import csv
import json
import math
from random import randint
from typing import Callable


#  Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def random_number_in_csv():
    count = randint(100, 1000)
    with open('data.csv', 'w') as file_csv:
        for i in range(1, count):
            stroka = f'{randint(1, 100)} {randint(1, 100)} {randint(1, 100)}'
            file_csv.write(stroka)
            file_csv.write('\n')


# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def read_csv(func: Callable):
    def wrapper():
        with open('data.csv', 'r') as file_csv:
            read = csv.reader(file_csv)
            for i, stroka in enumerate(read):
                row = str(stroka[0]).split(' ')
                input_number = [int(num) for num in row]
                result = func(input_number)
                print(result)
        return result

    return wrapper


# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def our_cashe(func: callable):
    try:
        with open(f'{func.__name__}.json', 'r', encoding='UTF-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    def wrapper(args):
        string_arg = str(args)
        result = func(args)
        data.update({string_arg: result})
        with open(f'{func.__name__}.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4)
        return result

    return wrapper


# Нахождение корней квадратного уравнения
@read_csv
@our_cashe
def roots(inp_num: list):
    a, b, c = inp_num[0], inp_num[1], inp_num[2]
    d = b ** 2 - 4 * a * c
    if d == 0:
        x = -(b / 2 * a)
        return f'Root: {round(x, 2)}'
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return f'Roots: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}'
    else:
        return 'No roots'


if __name__ == '__main__':
    random_number_in_csv()
    roots()
