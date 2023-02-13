def buy_sell_stocks(prices: []) -> int:
    n = len(prices)
    profit = 0
    buy = prices[0]
    for i in range(1, n):
        buy = min(buy, prices[i])
        profit = max(profit, prices[i] - buy)

    return profit


if __name__ == '__main__':
    print(buy_sell_stocks([4, 8, 1, 2, 5]))
    print(buy_sell_stocks([7, 1, 5, 3, 6, 4]))
    print(buy_sell_stocks([7, 6, 4, 3, 1]))
