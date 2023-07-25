# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
# Дополнительное:
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# * Какие вещи взяли все три друга
# * Какие вещи уникальны, есть только у одного друга
# * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# * Для решения используйте операции с множествами.
#   Код должен расширяться на любое большее количество друзей.

FRIENDS_IN_EXPEDITION = {'Андрей': {'Вода', 'Палатка', 'Спички', 'Котелок'},
                         'Вова': {'Фонарь', 'Рюкзак', 'Палатка', 'Вода'},
                         'Костя': {'Палатка', 'Розжиг', 'Мангал', 'Фонарь'}}


def find_joint_item(dict_base: dict) -> dict:
    data_keys = list(dict_base.keys())
    count = 1
    result = dict_base[data_keys[0]]
    while count != len(data_keys):
        result &= dict_base[data_keys[count]]
        count += 1
    return result


def find_unique_item(dict_base: dict) -> dict:
    data_keys = list(dict_base.keys())
    count = 1
    result = dict_base[data_keys[0]]
    while count != len(data_keys):
        result |= dict_base[data_keys[count]]
        count += 1
    return result


# * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
#  Почти доделал. Так думаю 😄

# def find_joint_item_except_one(dict_base: dict) -> dict:
#     data_keys = list(dict_base.keys())
#     count = 1
#     result = dict_base[data_keys[0]]
#     while count != len(data_keys):
#         temp = result
#         result &= dict_base[data_keys[count]]
#         if result == {}:
#             name = data_keys[count]
#             vesch = temp
#             result = temp
#             # fs[data_keys[count]] = temp
#             fs = {data_keys[name]: vesch}
#             return fs
#             continue
#         count += 1

print(f'Вещи, которые есть у всех: {find_joint_item(FRIENDS_IN_EXPEDITION)}')
print(f'Вещи, которые есть только у одного друга {find_unique_item(FRIENDS_IN_EXPEDITION)}')
