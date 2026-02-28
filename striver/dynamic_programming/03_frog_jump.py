"""
Given an integer array height[] where height[i] represents the height of the i-th stair,
a frog starts from the first stair and wants to reach the last stair.
From any stair i, the frog has two options:
it can either jump to the (i+1)th stair or the (i+2)th stair.
The cost of a jump is the absolute difference in height between the two stairs.
Determine the minimum total cost required for the frog to reach the last stair.

GFG -> https://www.geeksforgeeks.org/problems/geek-jump/0
"""


def min_jump_rec(height_arr):
    if len(height_arr) == 1:
        return 0
    return min_jump_rec_util(len(height_arr) - 1, height_arr)


def min_jump_rec_util(n, height_arr):
    if n == 0:
        return 0
    if n == 1:
        return abs(height_arr[1] - height_arr[0])

    option_1 = min_jump_rec_util(n - 1, height_arr) + abs(height_arr[n] - height_arr[n - 1])
    if n >= 2:
        option_2 = min_jump_rec_util(n - 2, height_arr) + abs(height_arr[n] - height_arr[n - 2])
        return min(option_1, option_2)
    else:
        return option_1


def min_jump_mem_util(n, dp, height_arr):
    if dp[n] != -1:
        return dp[n]
    one_step = min_jump_mem_util(n - 1, dp, height_arr) + abs(height_arr[n] - height_arr[n - 1])

    if n >= 2:
        two_step = min_jump_mem_util(n - 2, dp, height_arr) + abs(height_arr[n] - height_arr[n - 2])
        dp[n] = min(one_step, two_step)
        return dp[n]
    else:
        dp[n] = one_step
        return dp[n]


def min_jump_mem(height_arr):
    n = len(height_arr)
    dp = [-1] * n
    dp[0] = 0
    return min_jump_mem_util(n - 1, dp, height_arr)


def min_jump_tab(height_arr):
    n = len(height_arr)
    dp = [-1] * n
    dp[0] = 0
    for i in range(1, n):
        option_1 = dp[i - 1] + abs(height_arr[i - 1] - height_arr[i])
        if i >= 2:
            option_2 = dp[i - 2] + abs(height_arr[i - 2] - height_arr[i])
            dp[i] = min(option_1, option_2)
        else:
            dp[i] = option_1
    return dp[n - 1]


def min_jump_tab_space_optimised(height_arr):
    n = len(height_arr)
    prev = 0
    prev2 = 0
    for i in range(1, n):
        fs = prev + abs(height_arr[i] - height_arr[i - 1])
        if i > 1:
            ss = prev2 + abs(height_arr[i] - height_arr[i - 2])
            prev2 = prev
            prev = min(fs, ss)
        else:
            prev2 = prev
            prev = fs
    return prev


if __name__ == '__main__':
    print(min_jump_rec([30, 10, 60, 10]))
    print(min_jump_rec([30, 10, 60, 10, 60, 50]))
    print(min_jump_mem([30, 10, 60, 10, 60, 50]))
    print(min_jump_tab([30, 10, 60, 10]))
    print(min_jump_tab([30, 10, 60, 10, 60, 50]))
    print(min_jump_tab_space_optimised([30, 10, 60, 10, 60, 50]))
    print(min_jump_tab_space_optimised([10, 30, 40, 20, 50]))
