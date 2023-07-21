# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
import time

MAX_VALUE = 100000
CONVERT_IN_MILLISECONDS = 1000

def checking_for_a_prime_number(max_value: int, num: int):
    count = 0
    if 0 < num < max_value:
        start_time = time.time()
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                count += 1
        if count == 0:
            print(f'Число {num} является простым')
        else:
            print(f'Число {num} не является простым')
    else:
        print('Число вне диапозона.')
    end_time = time.time()
    print(f'--- Время работы: {(end_time - start_time) * CONVERT_IN_MILLISECONDS} миллисекунд ---')


run = True
while run:
    number = int(input('Введите число от 0 до 100 000: '))
    checking_for_a_prime_number(MAX_VALUE, number)
    if input('Продолжить? Да: введите все что захотите, НЕТ: "ENTER" ') == '':
        run = False
