"""
To reach to a n'th stair, I can either come from
n-1th stair or n-2th stair, so if we can get distinct ways to
reach to these two stairs, we just need to sum it up
Similar to fibonacci number
"""


def stairs_way(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == '__main__':
    print(stairs_way(100))
