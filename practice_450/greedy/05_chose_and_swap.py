def chose_and_swap(input_string: str):
    n = len(input_string)
    input_set = sorted(set(list(input_string)))
    dict_map = {}
    for i in range(0, len(input_set)):
        dict_map[input_set[i]] = 1

    # return dict_map
    chose = list(dict_map.keys())[0]
    replace = list(dict_map.keys())[0]
    for i in range(0, n):
        char = input_string[i]
        if char not in dict_map:
            continue
        smallest_char = list(dict_map.keys())[0]
        if smallest_char == char:
            del dict_map[char]
            continue
        elif char > smallest_char:
            chose = char
            replace = smallest_char
            break
        else:
            del dict_map[char]

    input_string_list = list(input_string)
    for i in range(0, n):
        curr_char = input_string_list[i]
        if curr_char == chose:
            input_string_list[i] = replace
        elif curr_char == replace:
            input_string_list[i] = chose

    return ''.join(input_string_list)





if __name__ == '__main__':
    print(chose_and_swap('ccad'))
    print(chose_and_swap('abba'))
    print(chose_and_swap('adcba'))
    print(chose_and_swap('abcdefghijklnm'))
