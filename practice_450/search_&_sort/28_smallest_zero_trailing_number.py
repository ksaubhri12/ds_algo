import math


def smallest_factorial(n: int):
    start = 0
    end = 100000
    answer = None
    while start <= end:
        middle = start + (end - start) // 2
        middle_factorial = get_factorial(middle)
        zero_count = get_number_of_zero(middle_factorial, 1, 0)
        if zero_count >= n:
            answer = middle
            end = middle - 1
        else:
            start = middle + 1

    return answer



def get_factorial(number):
    return math.factorial(number)


def get_number_of_zero(number, i, answer):
    divide_by = int(math.pow(10, i))
    if number % divide_by != 0:
        return answer
    else:
        answer = i
        i = i + 1
        return get_number_of_zero(number, i, answer)


if __name__ == '__main__':
    print(smallest_factorial(23))
    print(smallest_factorial(1))
    print(smallest_factorial(6))
    print(smallest_factorial(8))

    print(get_factorial(10))
    print(get_number_of_zero(12000, 1, 0))
