import math


def smallest_number(sum_value: int, digits: int):
    max_sum = 9 * digits
    if sum_value > max_sum:
        return "-1"
    curr_sum = 1
    number = str(int(math.pow(10, digits - 1)))

    return smallest_number_util(curr_sum, number, sum_value, digits)


def smallest_number_util(curr_sum: int, number: str, sum_need: int, digits: int):
    for i in reversed(range(0, digits)):
        if int(number[i]) == 0 or int(number[i]) == 1:
            remaining_sum = sum_need - curr_sum
            if remaining_sum >= 10:
                number_list = list(number)
                number_list[i] = str(9)
                curr_sum = curr_sum + 9
                number = ''.join(number_list)
                return smallest_number_util(curr_sum, number, sum_need, digits)

            else:
                number_list = list(number)
                value = int(number[i]) + remaining_sum
                number_list[i] = str(value)
                return ''.join(number_list)
        if int(number[i]) == 9:
            continue

    return '-1'


if __name__ == '__main__':
    print(smallest_number(20, 3))
    print(smallest_number(9, 2))
