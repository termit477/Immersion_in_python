"""
Создайте функцию генератор чисел Фибоначчи.
"""
import pprint


def fibonacci():
    fib1 = 0
    fib2 = 1
    for _ in range(N + 1):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


def fibonacci_in_dict(fib):
    iter_fibonacci = iter(fib)
    return {i: next(iter_fibonacci) for i in range(N + 1)}


run = True
while run:
    N = input('Введитие число или "ENTER" для выхода из программы: ')
    if N == '':
        run = False
    else:
        try:
            N = int(N)
            result_fibonacci = fibonacci()
            pprint.pprint(fibonacci_in_dict(result_fibonacci))
        except ValueError:
            print('Ошибка! \nВведите ЦЕЛОЕ ЧИСЛО или "ENTER" для выхода.')
