"""
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.

Пример:
test/users/names.txt
Результат в json для names.txt:
{
"name": names.txt
"parent": users,
"type": "file"
"size": 4096
}
"""
import csv
import json
import os.path
import pickle


def record_file(res: list):
    with (open('data.json', 'w', newline='') as file_json,
          open('data.csv', 'w', newline='') as file_csv,
          open('data.pickle', 'wb') as file_pickle):
        json.dump(res, file_json, indent=4)

        csv_writer = csv.DictWriter(file_csv, fieldnames=['name', 'parent', 'type', 'size'])
        csv_writer.writeheader()
        csv_writer.writerows(res)

        pickle.dump(res, file_pickle)


def get_size_dir(path: str) -> int:
    size = 0
    for (root, dirs, files) in os.walk(path, topdown=True):
        for item in files:
            if root == '.':
                path_file = item
            else:
                path_file = root + '\\' + item
            size += os.path.getsize(path_file)
    return size


def dir_walk(path: str) -> None:
    result = []
    for (root, dirs, files) in os.walk(path, topdown=True):
        parent = str(root).split('\\')[-1]
        if files is not None:
            for item in files:
                if root == '.':
                    path_file = item
                else:
                    path_file = root + '\\' + item
                result.append({'name': item,
                               'parent': parent,
                               'type': 'file',
                               'size': os.path.getsize(path_file)})
        if dirs is not None:
            for item in dirs:
                result.append({'name': item,
                               'parent': parent,
                               'type': 'dir',
                               'size': get_size_dir(path=root + '\\' + item)})
    record_file(result)


if __name__ == '__main__':
    dir_walk('.')
