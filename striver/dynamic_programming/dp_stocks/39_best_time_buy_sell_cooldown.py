def max_profit_tab(prices) -> int:
    n = len(prices)
    dp_arr = [[0 for _ in range(2)] for _ in range(n + 2)]
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
                sell_profit = prices[index] + dp_arr[index + 2][bool(True)]
                no_sell_profit = 0 + dp_arr[index + 1][bool(False)]
                profit = max(profit, sell_profit, no_sell_profit)
            dp_arr[index][buy] = int(profit)
    return dp_arr[0][bool(True)]


if __name__ == '__main__':
    print(max_profit_tab([0, 2, 1, 2, 3]))
    print(max_profit_tab([3, 1, 6, 1, 2, 4]))
