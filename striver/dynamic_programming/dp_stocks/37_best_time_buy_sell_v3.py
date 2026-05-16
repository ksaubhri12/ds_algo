"""
Similar to problem 36 but here I can't do more than 2 transaction
Idea is to use knapsack concept of reducing weight
"""


def max_profit_rec(prices: [], index: int, buy: bool, cap: int, dp_arr) -> int:
    if cap == 0:
        return 0

    if index == len(prices):
        return 0
    if dp_arr[index][bool(buy)][cap] != -1:
        return dp_arr[index][bool(buy)][cap]
    profit = float("-inf")
    if buy:
        buy_profit = -prices[index] + max_profit_rec(prices, index + 1, False, cap, dp_arr)
        no_buy_profit = max_profit_rec(prices, index + 1, True, cap, dp_arr)
        buy_profit = max(buy_profit, no_buy_profit)
        profit = max(profit, buy_profit)
    else:
        sell_profit = prices[index] + max_profit_rec(prices, index + 1, True, cap - 1, dp_arr)
        no_sell_profit = 0 + max_profit_rec(prices, index + 1, False, cap, dp_arr)
        sell_profit = max(sell_profit, no_sell_profit)
        profit = max(profit, sell_profit)
    dp_arr[index][bool(buy)][cap] = int(profit)
    return int(profit)


def max_profit(prices) -> int:
    n = len(prices)
    dp_arr = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
    return max_profit_rec(prices, 0, True, 2, dp_arr)


def max_profit_tab(prices) -> int:
    n = len(prices)
    dp_arr = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

    for index in reversed(range(n)):
        for buy in range(2):
            for cap in range(1, 3):
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

    return dp_arr[0][1][2]


if __name__ == '__main__':
    print(max_profit([10, 22, 5, 75, 65, 80]))
    print(max_profit([2, 30, 15, 10, 8, 25, 80]))
    print("tab")
    print(max_profit_tab([10, 22, 5, 75, 65, 80]))
    print(max_profit_tab([2, 30, 15, 10, 8, 25, 80]))
