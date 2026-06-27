"""
Best Time to Buy and Sell Stock  —  Easy
LC: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Statement:
    prices[i] is the price on day i. Buy on one day, sell on a LATER day.
    Return the max profit, or 0 if no profit is possible.

Constraints:
    1 <= len(prices) <= 1e5 ; 0 <= prices[i] <= 1e4

Pattern: Sliding Window / running-minimum (track min price so far)

--- fill in as you solve (brief 7) ---
Brute force:
Optimal idea (one pass: what do you track as you move right?):
Time / Space:
"""


def max_profit(prices: list[int]) -> int:
    pass


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))     # 0
