def rearrange_characters(input_string: str):
    n = len(input_string)
    dict_value = {}
    for i in range(0, n):
        if input_string[i] in dict_value:
            dict_value[input_string[i]] = dict_value[input_string[i]] + 1
        else:
            dict_value[input_string[i]] = 1

    sorted_count_list = sorted(dict_value, key=dict_value.get, reverse=True)
    i = 0
    start = 0
    char_list = list(input_string)
    while len(sorted_count_list) > 0:
        char = sorted_count_list.pop(0)
        count = dict_value[char]
        if count > n / 2:
            return -1
        start = start + 1
        for k in range(0, count):
            char_list[i] = char
            i = i + 2
            if i >= n:
                i = 1

    return ''.join(char_list)


if __name__ == '__main__':
    print(rearrange_characters('geeksforgeeks'))
    print(rearrange_characters('bbbbb'))
    print(rearrange_characters('kkk'))
