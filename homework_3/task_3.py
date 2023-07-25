# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# * Верните все возможные варианты комплектации рюкзака.
from random import randint

MAX_WEIGHT = 12
BACKPACK = 0
ITEM_IN_BACKPACK = []
ITEM_FOR_EXPEDITION = {'Спички': 1,
                       'Туалетная бумага': 1,
                       'Вода': 5,
                       'Еда': 3,
                       'Фонарик': 1,
                       'Котелок': 3,
                       'Палатка': 4,
                       'Розжиг': 1}


def filling_the_backpack(item: dict, bag: int, item_in_bag: list) -> list:
    for key, value in item.items():
        if bag + value <= MAX_WEIGHT:
            bag += value
            item_in_bag.append(key)
        else:
            continue
    return item_in_bag


print(f'Вариант коплектации рюкзака: {filling_the_backpack(ITEM_FOR_EXPEDITION, BACKPACK, ITEM_IN_BACKPACK)}')
