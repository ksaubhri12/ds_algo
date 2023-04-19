def print_permutation(input_string: str, result_arr: [], output_string: str, result_map: {}, n):
    if n < 0:
        return

    if n == 0:
        if output_string not in result_map:
            result_map[output_string] = 1
            result_arr.append(output_string)

        return

    for i in range(n):
        new_string = remove_string(input_string, i)
        print_permutation(new_string, result_arr, output_string + input_string[i], result_map, n - 1)


def remove_string(input_string, index):
    left = input_string[:index]
    right = input_string[index + 1:]
    return left + right


def print_permutation_driver(input_string: str):
    result_map = {}
    result_arr = []
    print_permutation(input_string, result_arr, '', result_map, len(input_string))
    return result_arr


if __name__ == '__main__':
    print(print_permutation_driver('ABC'))
