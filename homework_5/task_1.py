"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import os
import pprint


def absolute_path(full_path_to_file: str) -> tuple:
    temp = full_path_to_file.split('\\')
    full_name_file = temp.pop().split('.')
    path_to_file = '->'.join(temp)
    name_file = full_name_file[0]
    expansion = full_name_file[1]
    result = (path_to_file, name_file, expansion,)
    return result


path = os.path.abspath('task.py')
pprint.pprint(absolute_path(path))
