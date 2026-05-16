def best_time_buy_sell(stock_prices: []) -> []:
    n = len(stock_prices)
    min_price = stock_prices[0]
    profit = 0
    for stock_price_index in range(1, n):
        stock_price = stock_prices[stock_price_index]
        min_price = min(stock_price, min_price)
        profit = max(profit, stock_price - min_price)

    return profit


if __name__ == '__main__':
    print(best_time_buy_sell([7, 1, 5, 3, 6, 4]))
