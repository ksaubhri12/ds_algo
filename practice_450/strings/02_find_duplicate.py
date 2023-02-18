def find_duplicate(value: str):
    count_dict = {}
    n = len(value)
    for i in range(0, n):
        element = value[i]
        if element in count_dict:
            count_dict[element] = count_dict[element] + 1
        else:
            count_dict[element] = 1

    for key in count_dict.keys():
        count = count_dict[key]
        if count > 1:
            print(key)


def find_duplicate_v2(value: str):
    char_arr = [0] * 256
    n = len(value)
    for i in range(0, n):
        element = value[i]
        order = ord(element)
        char_arr[order] = char_arr[order] + 1

    n = len(char_arr)
    for i in range(0, n):
        count = char_arr[i]
        if count > 1:
            print(chr(i))


if __name__ == '__main__':
    print(find_duplicate_v2("kalpeshk"))
