def min_sum_two_number(input_arr: [], n: int):
    if len(input_arr) == 0:
        return 0

    if len(input_arr) == 1:
        return input_arr[0]

    input_arr = sorted(input_arr)

    string_1 = ''
    string_2 = ''
    i = 0
    while i < n:
        string_1 = string_1 + str(input_arr[i])
        i = i + 1
        if i < n:
            string_2 = string_2 + str(input_arr[i])
            i = i + 1

    value_1 = int(string_1)
    value_2 = int(string_2)
    return value_2 + value_1


if __name__ == '__main__':
    print(min_sum_two_number([6, 8, 4, 5, 2, 3], 6))

    print(min_sum_two_number([5, 3, 0, 7, 4], 5))
