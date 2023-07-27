# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

COMM_WITHDRAWAL = 1.5
COMM_REFILL = 3
TAX = 10
COMM_MIN = 30
COMM_MAX = 600
SUM_WORK = 50
MAX_ACCOUNT = 5_000_000

account = 0
count_refill = 0
count_withdrawal = 0


def get_money() -> int:
    while True:
        try:
            num = int(input('Введите сумму: '))
            if num > 0 and num % SUM_WORK == 0:
                return num
            else:
                print('Введите положительную сумму кратную 50.')
        except ValueError:
            print('Что то пошло не так.')


def refill_account(num: int):
    global account
    account += num


def account_proc():
    global account
    num = account / 100 * COMM_REFILL
    refill_account(num)


def take_account(num: int):
    global account
    account -= num


def take_tax():
    global account
    if account > MAX_ACCOUNT:
        num = account / 100 * TAX
        take_account(int(num))


def check_money(num) -> int:
    proc = num / 100 * COMM_WITHDRAWAL
    if proc < COMM_MIN:
        num += COMM_MIN
    elif proc > COMM_MAX:
        num += COMM_MAX
    else:
        num += proc
    return num


print('Банкомат открыт.')
while True:
    choice = input('Выберите действие: \n'
                   '1 - Пополнить счет \n'
                   '2 - Снять деньги \n'
                   'ENTER - выход из банкомата\n')
    match choice:
        case '1':
            number = get_money()
            take_tax()
            refill_account(number)
            count_refill += 1
            if count_refill == 3:
                account_proc()
                count_refill = 0
            print(f'У Вас на счету: {account} рублей.')
            print()
        case '2':
            number = get_money()
            take_tax()
            number = check_money(number)
            if number < account:
                take_account(number)
                count_withdrawal += 1
                if count_withdrawal == 3:
                    account_proc()
                    count_withdrawal = 0
                print(f'У Вас на счету: {account} рублей.')
            else:
                print('Недостаточно средств.')
                print(f'У Вас на счету: {account} рублей.')
                print()
        case '':
            print(f'У Вас на счету: {account} рублей.')
            print('До свидания')
            break
