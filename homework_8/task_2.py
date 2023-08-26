"""
Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.
"""
import csv
import json
import pickle
from os import chdir


def convert_to_json(old_file: str, new_file: str):
    chdir('..')
    chdir('seminar_7')
    with open(old_file, 'r') as read_file:
        data = read_file.read().split('\n')[:-1]
        data = [{i.split()[0].capitalize():
                     float(i.split()[1])} for i in data]
        print(data)
    with open(new_file, 'w') as write_file:
        json.dump(data, write_file, indent=4)


def enter_data(name_file: str) -> None:
    while True:
        id = int(input('Введите id: '))
        name = input('Введите имя: ')
        level = input('Введите уровень доступа: ')
        try:
            with open(name_file, 'r', encoding='utf-8') as file:
                new_dict: dict = json.load(file)
        except:
            new_dict = {str(i): {} for i in range(1, 8)}
        if check_id(new_dict, id):
            new_dict[level].update({id: name})
        else:
            continue

        with open(name_file, 'w', encoding='utf-8') as new_file:
            json.dump(new_dict, new_file, indent=2)


def check_id(data: dict, id: str) -> bool:
    for item in data.values():
        if id in item.keys():
            return False
    return True


def json_csv(name_file: str):
    with open(f'{name_file}.json', 'r') as file:
        data = json.load(file)
    rows = []
    for level, users in data.items():
        for id, name in users.items():
            rows.append({'level': level,
                         'name': name,
                         'id': id})
    with open('task_3.csv', 'w', newline='') as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames=['level', 'name', 'id'])
        csv_writer.writeheader()
        csv_writer.writerows(rows)


def json_to_csv(name_file: str):
    with open(f'{name_file}.csv', 'r', newline='') as file:
        data = file.read().split('\n')

    res = []
    data.pop()
    for value in data[1:]:
        print(value)
        level, name, id = value[:-1].split(',')
        res.append({'level': level, 'id': f'{int(id):03}', 'name': name, 'hash': hash(id + name)})

    with open('task_4.json', 'w', newline='') as new_file:
        json.dump(res, new_file, indent=4)


def json_to_pickle(dir: str):
    files = list(filter(lambda x: '.json' in x, os.listdir()))
    for file in files:
        filename, *_ = file.split('.')
        with (open(file, 'r') as sourse, open(f'{filename}.pickle', 'wb') as res):
            data = json.load(sourse)
            pickle.dump(data, res)
