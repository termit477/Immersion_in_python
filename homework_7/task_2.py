"""
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""
from os import chdir, listdir, getcwd, mkdir
from pathlib import Path
from random import randint, uniform, choice


# Запись в файл чисел
def writing_file(name_file: str, count: int) -> None:
    name_file += '.txt'
    with open(name_file, 'a', encoding='utf-8') as file:
        for i in range(count):
            file.write(f'{randint(-1000, 1000)} | {uniform(-1000, 1000)} \n')


# Подбор рандомного названия файла
def give_name() -> str:
    name = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


# Соединение файлов с рандомными названиями и числами
def join_files(name_file_names: str, name_file_numbers: str, name_file_output: str) -> None:
    name_file_names += '.txt'
    name_file_numbers += '.txt'
    name_file_output += '.txt'
    with (open(name_file_names, 'r', encoding='utf-8') as file_names,
          open(name_file_numbers, 'r', encoding='utf-8') as file_numbers):
        names = file_names.read().split('\n')
        numbers = file_numbers.read().split('\n')

    if len(numbers) > len(names):
        names += names[:len(numbers) - len(names)]
    else:
        numbers += numbers[:len(names) - len(numbers)]

    with open(name_file_output, 'a', encoding='utf-8') as file_output:
        for name, number in zip(names, numbers):
            if not name or not number:
                break
            number_output_int, number_output_float = map(float, number.split(' | '))
            mult = number_output_int * number_output_float
            if mult < 0:
                file_output.write(f'{name.lower()} {abs(mult)} \n')
            else:
                file_output.write(f'{name.upper()} {int(mult)} \n')


# Создание файлов с информацией в байтовом виде
def create_file(min_len: int = 6,
                max_len: int = 30,
                min_size: int = 256,
                max_size: int = 4096,
                count_files: int = 42):
    for _ in range(count_files):
        ext = choice(('.txt', '.doc', '.xml'))
        with open(give_name() + ext, 'w', encoding='utf-8') as file:
            list_of_bytes = bytes([randint(0, 255) for i in range(min_size, max_size)])
            file.write(str(list_of_bytes))


# Сортировка файлов по папкам-форматам файлов.
def sort_files(direc: str | Path):
    chdir(direc)
    print(listdir())
    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue
        ext = file.name.split('.')[1]
        if ext.upper() not in listdir():
            mkdir(ext.upper())
        file.replace(f'{ext.upper()}\\{file.name}')
