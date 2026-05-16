"""
I can buy it as many times as I want and then I have to sell it
I can do multiple transaction but the rules remains same
I can't sell before buying it
Before performing next buy, you have to sell it for sure
"""


def max_profit_rec(prices, index, buy, dp_arr) -> int:
    if index >= len(prices):
        return 0

    if dp_arr[index][int(buy)] != -1:
        return dp_arr[index][int(buy)]

    buy_profit = float("-inf")
    sell_profit = float("-inf")
    if buy:
        buy_profit = -prices[index] + max_profit_rec(prices, index + 1, False, dp_arr)
        no_buy_profit = 0 + max_profit_rec(prices, index + 1, True, dp_arr)
        buy_profit = max(buy_profit, no_buy_profit)
    else:
        sell_profit = prices[index] + max_profit_rec(prices, index + 1, True, dp_arr)
        no_sell_profit = 0 + max_profit_rec(prices, index + 1, False, dp_arr)
        sell_profit = max(sell_profit, no_sell_profit)

    dp_arr[index][int(buy)] = max(buy_profit, sell_profit)
    return dp_arr[index][int(buy)]


def max_profit(prices) -> int:
    dp_arr = [[-1 for _ in range(2)] for _ in range(len(prices))]
    return max_profit_rec(prices, 0, True, dp_arr)


def max_profit_tab(prices) -> int:
    n = len(prices)
    dp_arr = [[-1 for _ in range(2)] for _ in range(n + 1)]
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
                sell_profit = prices[index] + dp_arr[index + 1][bool(True)]
                no_sell_profit = 0 + dp_arr[index + 1][bool(False)]
                profit = max(profit, sell_profit, no_sell_profit)
            dp_arr[index][buy] = int(profit)
    return dp_arr[0][bool(True)]


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit_tab([7, 1, 5, 3, 6, 4]))
