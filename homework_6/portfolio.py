"""
Вы являетесь инвестором и хотите создать программу для расчета нескольких финансовых показателей вашего портфеля акций.
Создайте модуль Python под названием "portfolio.py", который будет содержать функции для выполнения следующих операций:

Расчет общей стоимости портфеля акций:
Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float принимает два аргумента:
stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.),
и значениями - количество акций каждого символа.
prices - словарь, где ключами являются символы акций, а значениями - текущая цена каждой акции.
Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен.

Расчет доходности портфеля:
Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float принимает два аргумента:
initial_value - начальная стоимость портфеля акций.
current_value - текущая стоимость портфеля акций.
Функция должна вернуть процентную доходность портфеля.

Определение наиболее прибыльной акции:
Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str принимает два аргумента:
stocks - словарь с акциями и их количеством.
prices - словарь с акциями и их текущими ценами.
Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью.

Тестирование модуля:
Напишите небольшую программу, которая импортирует модуль "portfolio.py" и демонстрирует использование всех трех функций.
Создайте словари для акций и цен, запустите функции и выведите результаты.

Примечание:
В реальном мире вы можете использовать API для получения актуальных данных о ценах акций. В данной задаче можно
использовать фиктивные данные для тестирования и обучения.
"""
import operator
import random
from functools import reduce
import yfinance as yf


# Получение цен акций
def get_price(stock: str, days_ago: int) -> float:
    ticker = yf.Ticker(stock)
    return round(ticker.history(period=str(days_ago) + 'd')['Close'][0], 2)


# Получение списка начальных цен акций
def creating_prices(ticker_list: list, days_ago: int) -> dict:
    return {i: get_price(i, days_ago) for i in ticker_list}


# Создание портфеля
def creating_portfolio(ticker_list: list) -> dict:
    return {i: random.randint(1, 20) for i in ticker_list}


# Получение суммы цен акций
def sum_value_prices(price: dict) -> float:
    return round(sum(price.values()), 2)


# Получение стоимость портфеля акций
def calculate_portfolio_value(stocks: dict, price: dict) -> float:
    all_prices = {key: round(value * price[key], 2) for key, value in stocks.items()}
    return reduce(lambda x, y: x + y, all_prices.values())


# Получение процентной доходности портфеля
def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return round((current_value - initial_value) / initial_value * 100, 2)


# Акция, имеющая наибольшую прибыль
def get_most_profitable_stock(stocks: dict, price: dict, begin_price: dict) -> str:
    all_prices = {key: round((value - begin_price[key]) * stocks[key], 2) for key, value in price.items()}
    return max(all_prices.items(), key=operator.itemgetter(1))[0]
