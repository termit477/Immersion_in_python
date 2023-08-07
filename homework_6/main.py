from portfolio import *

buy_stock_days_ago = 100
tickers_list = ['AAPL', 'TSLA', 'AMD', 'NVDA', 'MSFT']

prices = creating_prices(tickers_list, 0)
begin_prices = creating_prices(tickers_list, buy_stock_days_ago)

portfolio = creating_portfolio(tickers_list)


sum_begin_prices = sum_value_prices(begin_prices)
sum_prices = sum_value_prices(prices)

print(f'{calculate_portfolio_value(portfolio, prices)} $')
print(f'{calculate_portfolio_return(sum_begin_prices, sum_prices)} %')
print(f'{get_most_profitable_stock(portfolio, prices, begin_prices)}')
