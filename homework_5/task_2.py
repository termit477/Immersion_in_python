"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
"""
import pprint


def create_dict(name_list: list[str], salary_list: list[int], bonus_list: list[str]) -> dict:
    zip_list = list(zip(name_list, salary_list, bonus_list))
    result_dict = {}
    for elem in zip_list:
        result_dict[elem[0]] = int(elem[1] + elem[1] / 100 * float(elem[2].replace('%', '')))
    return result_dict


def gen_create_dict(name_list: list[str], salary_list: list[int], bonus_list: list[str]) -> dict:
    return {name_list[i]: int(salary_list[i] + salary_list[i] / 100 * float(bonus_list[i].replace('%', '')))
            for i in range(len(name_list))}

print('С помощью обычной функции:')
names = ['Дима', 'Марина', 'Андрей', 'Никита', 'Костя']
salary = [50_000, 35_000, 65_000, 40_000, 100_000]
bonus = ['10%', '5.5%', '12.5%', '9.25%', '15%']
pprint.pprint(create_dict(names, salary, bonus))
print()
print('С помощью генерации списка:')
pprint.pprint(gen_create_dict(names, salary, bonus))
