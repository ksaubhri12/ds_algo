def max_profit_tab(prices, k) -> int:
    n = len(prices)
    dp_arr = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]

    for index in reversed(range(n)):
        for buy in range(2):
            for cap in range(1, k + 1):
                profit = float("-inf")
                if buy:
                    buy_profit = -prices[index] + dp_arr[index + 1][bool(False)][cap]
                    no_buy_profit = dp_arr[index + 1][bool(True)][cap]
                    buy_profit = max(buy_profit, no_buy_profit)
                    profit = max(profit, buy_profit)
                else:
                    sell_profit = prices[index] + dp_arr[index + 1][bool(True)][cap - 1]
                    no_sell_profit = dp_arr[index + 1][bool(False)][cap]
                    sell_profit = max(sell_profit, no_sell_profit)
                    profit = max(profit, sell_profit)
                dp_arr[index][bool(buy)][cap] = int(profit)

    return dp_arr[0][1][k]


if __name__ == '__main__':
    print(max_profit_tab([2, 4, 1], 2))
    print(max_profit_tab([3,2,6,5,0,3], 2))
