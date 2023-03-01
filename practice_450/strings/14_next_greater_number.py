def next_greater_num(string_value: str):
    n = len(string_value)
    index_1 = None
    index_2 = None

    for i in reversed(range(0, n - 1)):
        if string_value[i] < string_value[i + 1]:
            index_1 = i
            break

    if index_1 is None:
        return string_value[::-1]

    min_diff = float('inf')
    for i in range(index_1 + 1, n):
        element = string_value[i]
        diff = int(element) - int(string_value[index_1])
        if min_diff > diff > 0:
            index_2 = i
            min_diff = diff

    string_array = list(string_value)
    string_array[index_1], string_array[index_2] = string_array[index_2], string_array[index_1]
    string_array[index_1 + 1: n] = reversed(string_array[index_1 + 1:n])

    return ''.join(string_array)


if __name__ == '__main__':
    print(next_greater_num('123654'))
