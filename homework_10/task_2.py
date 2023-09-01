"""
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.
"""

import operator
import random
from functools import reduce
import yfinance as yf


# Портфель
class Portfolio:
    def __init__(self, buy_stock_days_ago: int, tickers_list=None):
        if tickers_list is None:
            self.tickers_list = ['AAPL', 'TSLA', 'AMD', 'NVDA', 'MSFT']
        else:
            self.tickers_list = tickers_list
        self.buy_stock_days_ago = buy_stock_days_ago

    # Получение цен акций
    def _get_price(self, stock: str, days_ago: int) -> float:
        ticker = yf.Ticker(stock)
        return round(ticker.history(period=str(days_ago) + 'd')['Close'][0], 2)

    # Получение списка начальных цен акций
    def creating_prices(self, days_ago: int) -> dict:
        return {i: self._get_price(i, days_ago) for i in self.tickers_list}

    # Получение суммы цен акций
    def sum_value_prices(self, price: dict) -> float:
        return round(sum(price.values()), 2)

    # Создание портфеля
    def creating_portfolio(self) -> dict:
        return {i: random.randint(1, 20) for i in self.tickers_list}

    # Получение стоимость портфеля акций
    def calculate_portfolio_value(self) -> float:
        all_prices = {key: round(value * self.creating_prices(0)[key], 2)
                      for key, value in self.creating_portfolio().items()}
        return reduce(lambda x, y: x + y, all_prices.values())

    # Получение процентной доходности портфеля
    def calculate_portfolio_return(self) -> float:
        return round(self.sum_value_prices(self.creating_prices(0)) -
                     self.sum_value_prices(self.creating_prices(self.buy_stock_days_ago)) /
                     self.sum_value_prices(self.creating_prices(self.buy_stock_days_ago)) * 100, 2)

    # Акция, имеющая наибольшую прибыль
    def get_most_profitable_stock(self) -> str:
        all_prices = {key: round((value - self.creating_prices(self.buy_stock_days_ago)[key]) *
                                 self.creating_prices(self.buy_stock_days_ago)[key], 2)
                      for key, value in self.creating_prices(0).items()}
        return max(all_prices.items(), key=operator.itemgetter(1))[0]


def run_stock_portfolio():
    portfolio = Portfolio(100)

    print(f'{portfolio.calculate_portfolio_value()} $')
    print(f'{portfolio.calculate_portfolio_return()} %')
    print(f'{portfolio.get_most_profitable_stock()}')


# -----------------------------------------------------------------------

# Банкомат

class ATM:
    COMM_WITHDRAWAL = 1.5
    COMM_REFILL = 3
    TAX = 10
    COMM_MIN = 30
    COMM_MAX = 600
    SUM_WORK = 50
    MAX_ACCOUNT = 5_000_000

    def __init__(self, money: int,
                 count_refill: int,
                 count_withdrawal: int):

        self.money = money
        self.count_refill = count_refill
        self.count_withdrawal = count_withdrawal

    def get_money(self):
        while True:
            try:
                num = int(input('Введите сумму: '))
                if num > 0 and num % self.SUM_WORK == 0:
                    return num
                else:
                    print('Введите положительную сумму кратную 50.')
            except ValueError:
                print('Что то пошло не так.')

    def refill_account(self, num: int):
        self.money += num

    def take_account(self, num: int):
        self.money -= num

    def account_proc(self):
        num = int(self.money / 100 * self.COMM_REFILL)
        self.refill_account(num)

    def take_tax(self):
        if self.money > self.MAX_ACCOUNT:
            num = self.money / 100 * self.TAX
            self.take_account(int(num))

    def check_money(self, num: int):
        proc = num / 100 * self.COMM_WITHDRAWAL
        if proc < self.COMM_MIN:
            num += self.COMM_MIN
        elif proc > self.COMM_MAX:
            num += self.COMM_MAX
        else:
            num += proc
        return num


def run_ATM():
    print('Банкомат открыт.')
    current_account = ATM(0, 0, 0)
    while True:
        choice = input('Выберите действие: \n'
                       '1 - Пополнить счет \n'
                       '2 - Снять деньги \n'
                       'ENTER - выход из банкомата\n')
        match choice:
            case '1':
                number = current_account.get_money()
                current_account.take_tax()
                current_account.refill_account(number)
                current_account.count_refill += 1
                if current_account.count_refill == 3:
                    current_account.account_proc()
                    current_account.count_refill = 0
                print(f'У Вас на счету: {current_account.money} рублей.')
                print()

            case '2':
                number = current_account.get_money()
                current_account.take_tax()
                number = current_account.check_money(number)
                if number < current_account.money:
                    current_account.take_account(number)
                    current_account.count_withdrawal += 1
                    if current_account.count_withdrawal == 3:
                        current_account.account_proc()
                        current_account.count_withdrawal = 0
                    print(f'У Вас на счету: {current_account.money} рублей.')
                else:
                    print('Недостаточно средств.')
                    print(f'У Вас на счету: {current_account.money} рублей.')
                    print()

            case '':
                print(f'У Вас на счету: {current_account.money} рублей.')
                print('До свидания')
                break


if __name__ == '__main__':
    run_ATM()
    print('Ожидайте, расчитывается задача с портфелем')
    run_stock_portfolio()
