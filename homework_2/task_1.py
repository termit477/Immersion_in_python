# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def convert_in_16_system(num: str) -> str:
    num = int(num)
    result = ''
    while num > 0:
        tailing = num % 16
        match tailing:
            case 10:
                result += 'a'
            case 11:
                result += 'b'
            case 12:
                result += 'c'
            case 13:
                result += 'd'
            case 14:
                result += 'e'
            case 15:
                result += 'f'
            case _:
                result += str(tailing)
        num //= 16
    return result[::-1]


run = True
while run:
    input_number = input('Введите целое число или "ENTER" чтобы завершить программу: ')
    if input_number == '':
        print('Программа завершена')
        run = False
    else:
        print(convert_in_16_system(input_number), hex(int(input_number)), sep=', ')
