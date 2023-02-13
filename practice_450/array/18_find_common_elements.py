def find_common_elements(arr1: [], arr2: [], arr3: [], n1, n2, n3):
    dict_1 = {}
    dict_2 = {}
    dict_3 = {}
    set_arr_dict_from_arr(arr1, n1, dict_1)
    set_arr_dict_from_arr(arr2, n2, dict_2)
    set_arr_dict_from_arr(arr3, n3, dict_3)
    present_arr = []
    for key in dict_1.keys():
        if key in dict_2 and key in dict_3:
            present_arr.append(key)

    return present_arr.sort()


def set_arr_dict_from_arr(arr: [], n, arr_dict: {}):
    for i in range(0, n):
        element = arr[i]
        arr_dict[element] = 1
