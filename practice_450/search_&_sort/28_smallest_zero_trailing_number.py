import math


def smallest_factorial(n: int):
    start = 0
    end = int(math.pow(10, 5))
    divide_check = int(math.pow(10, n))
    dp = [-1] * (end + 1)
    dp[0] = 1
    dp[1] = 1
    answer = float('inf')
    while start <= end:
        middle = start + (end - start) // 2
        fact_num = get_factorial(middle, dp)
        is_n_zero = fact_num % divide_check == 0
        if is_n_zero:
            answer = min(answer, middle)
            end = middle - 1
        else:
            start = middle + 1

    return answer


def get_factorial(number, dp: []):
    return math.factorial(number)

    if number == 1:
        dp[1] = 1
        return 1
    if number == 0:
        dp[0] = 1
        return 1

    if dp[number] != -1:
        return dp[number]
    if dp[number - 1] != -1:
        dp[number] = number * dp[number - 1]
        return dp[number]
    dp[number] = number * get_factorial(number - 1, dp)
    return dp[number]

if __name__ == '__main__':
    # print(get_factorial())
    print(smallest_factorial(1))
    print(smallest_factorial(2))
    print(smallest_factorial(3))
    print(smallest_factorial(4))
    print(smallest_factorial(5))
    print(smallest_factorial(6))
    print(smallest_factorial(7))
    print(smallest_factorial(23))

