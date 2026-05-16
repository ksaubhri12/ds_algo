def max_profit_tab(prices, transaction_fees) -> int:
    n = len(prices)
    dp_arr = [[0 for _ in range(2)] for _ in range(n + 1)]
    dp_arr[n][0] = 0
    dp_arr[n][1] = 0
    for index in reversed(range(n)):
        for buy in range(2):
            profit = float("-inf")
            if bool(buy):
                buy_profit = -prices[index] + dp_arr[index + 1][bool(False)]
                no_buy_profit = 0 + dp_arr[index + 1][bool(True)]
                profit = max(profit, buy_profit, no_buy_profit)
            else:
                sell_profit = -transaction_fees + prices[index] + dp_arr[index + 1][bool(True)]
                no_sell_profit = 0 + dp_arr[index + 1][bool(False)]
                profit = max(profit, sell_profit, no_sell_profit)
            dp_arr[index][buy] = int(profit)
    return dp_arr[0][bool(True)]


if __name__ == '__main__':
    print(max_profit_tab([6, 1, 7, 2, 8, 4], 2))
    print(max_profit_tab([7, 1, 5, 3, 6, 4], 1))
