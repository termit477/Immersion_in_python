"""
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
Пример, когда задача решена верно:
_table = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
]
_SAFE_COMB_EXAMPLE = [(0, 0), (6, 1), (4, 2), (7, 3),
(1, 4), (3, 5), (5, 6), (2, 7)]
"""

_SAFE_COMB_EXAMPLE = [(0, 0), (6, 1), (4, 2), (7, 3),
                      (1, 4), (3, 5), (5, 6), (2, 7)]


def check_intersection() -> bool:
    correct = True
    for i in range(len(_SAFE_COMB_EXAMPLE)):
        for j in range(i + 1, len(_SAFE_COMB_EXAMPLE)):
            if _SAFE_COMB_EXAMPLE[i][0] == _SAFE_COMB_EXAMPLE[j][0] or \
                    _SAFE_COMB_EXAMPLE[i][1] == _SAFE_COMB_EXAMPLE[j][1] or \
                    abs(_SAFE_COMB_EXAMPLE[i][0] - _SAFE_COMB_EXAMPLE[j][0]) == \
                    abs(_SAFE_COMB_EXAMPLE[i][1] - _SAFE_COMB_EXAMPLE[j][1]):
                correct = False
    return correct


print(check_intersection())