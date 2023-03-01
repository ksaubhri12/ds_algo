def print_permutation(value: str, output: str, result: {}, result_arr: []):
    n = len(value)
    if n == 0:
        if output not in result:
            result[output] = 1
            result_arr.append(output)
        return

    for i in range(0, n):
        element = value[i]
        new_string = remove_element_from_string(value, i)
        print_permutation(new_string, output + element, result, result_arr)


def print_permutation_main_code(value: str):
    result = {}
    output = ''
    result_arr = []
    print_permutation(''.join(sorted(value)), output, result, result_arr)
    return result_arr


def remove_element_from_string(value: str, index: int):
    value = value[:index] + value[index + 1:]
    return value


if __name__ == '__main__':
    # print(print_permutation_main_code('ABC'))
    print(print_permutation_main_code('ljr'))
