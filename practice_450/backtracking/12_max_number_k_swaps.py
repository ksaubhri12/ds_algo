def max_number_k_swaps(input_string: str, k: int, result_arr: [], n):
    if k < 0:
        return
    if k == 0:
        final_int = int(input_string)
        result_arr[0] = max(final_int, result_arr[0])

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if int(input_string[i]) < int(input_string[j]):
                swapped_string = get_new_swapped_string(input_string, i, j)
                result_arr[0] = max(int(swapped_string), result_arr[0])
                max_number_k_swaps(swapped_string, k - 1, result_arr, n)


def get_new_swapped_string(input_string: str, i, j):
    val = input_string
    val_list = list(val)
    val_list[i], val_list[j] = val_list[j], val_list[i]
    return ''.join(val_list)


def max_swaps_driver(input_string: str, k: int):
    n = len(input_string)
    result_arr = [int(input_string)]
    max_number_k_swaps(input_string, k, result_arr, n)
    return result_arr[0]


if __name__ == '__main__':
    print(max_swaps_driver('1234567', 4))
    print(max_swaps_driver('3435335', 3))
