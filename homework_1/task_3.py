# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

NUMBER_OF_TRYING = 10


def guess_the_number(trying: int):
    search_number = randint(1, 1001)
    print('Угадайте число, загаданное программой в диапозоне от 0 до 1000')
    while trying > 0:
        users_number = int(input('Введите число, загаданное программой: '))
        trying -= 1
        if users_number > search_number:
            print(f'Загаданное число меньше вашего. Осталось попыток {trying}')
        elif users_number < search_number:
            print(f'Загаданное число больше вашего. Осталось попыток {trying}')
        else:
            print(f'Вы угадали число! Поздравляю! Было загадано число {search_number}')
            break


guess_the_number(NUMBER_OF_TRYING)
