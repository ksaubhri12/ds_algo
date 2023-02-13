def subset_another_array(arr1: [], arr2: [], n, m):
    dict_1 = {}

    dict_2 = {}

    set_dict_from_arr(arr1, n, dict_1)
    set_dict_from_arr(arr2, m, dict_2)

    for key in dict_2.keys():
        if key not in dict_1:
            return 'No'
        else:
            count_key = dict_2[key]
            count_in_another = dict_1[key]
            if count_in_another != count_key:
                return 'No'

    return 'Yes'


def set_dict_from_arr(arr: [], n, arr_dict: {}):
    for i in range(0, n):
        element = arr[i]
        if element in arr_dict:
            arr_dict[element] = arr_dict[element] + 1
        else:
            arr_dict[element] = 1


if __name__ == '__main__':
    print(subset_another_array([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 1], 8, 4))
    # print(subset_another_array([10, 5, 2, 23, 19], [19, 5, 3], 5, 3))
    # print(subset_another_array([1, 2, 3, 4, 5, 6], [1, 2, 4], 6, 3))
    # print(subset_another_array([11, 1, 13, 21, 3, 7], [11, 3, 7, 1], 6, 3))
