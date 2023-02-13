def get_pairs(arr: [], n, k):
    arr_dict = {}
    for i in range(0, n):
        element = arr[i]
        if element in arr_dict:
            arr_dict[element] = arr_dict[element] + 1
        else:
            arr_dict[element] = 1

    pair_count = 0
    for key in arr_dict.keys():
        other_key = k - key
        exist = other_key in arr_dict
        if exist:
            if other_key == key:
                if arr_dict[key] >= 2:
                    pair_count = pair_count + 1
                    print(pair_count, key, other_key)
            else:
                pair_count = pair_count + 1
                print(pair_count, key, other_key)

    return pair_count


if __name__ == '__main__':
    # print(get_pairs([1, 5, 7, 1], 4, 6))
    print(get_pairs(
        [48, 24, 99, 51, 33, 39, 29, 83, 74, 72, 22, 46, 40, 51, 67, 37, 78, 76, 26, 28, 76, 25, 10, 65, 64, 47, 34, 88,
         26, 49, 86, 73, 73, 36, 75, 5, 26, 4, 39, 99, 27, 12, 97, 67, 63, 15, 3, 92, 90], 49, 50))
