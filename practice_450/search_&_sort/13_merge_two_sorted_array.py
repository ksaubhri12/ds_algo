def merge_two_sorted_array(arr_1: [], n1: int, arr_2: [], n2: int):
    len_3 = n1 + n2
    arr_3 = [None] * len_3
    n1_start = 0
    n2_start = 0

    for i in range(0, len_3):
        if n1_start >= n1:
            arr_3[i] = arr_2[n2_start]
            n2_start = n2_start + 1
            continue

        if n2_start >= n2:
            arr_3[i] = arr_1[n1_start]
            n1_start = n1_start + 1
            continue

        n1_element = arr_1[n1_start]
        n2_element = arr_2[n2_start]

        if n1_element < n2_element:
            n1_start = n1_start + 1
            arr_3[i] = n1_element

        else:
            n2_start = n2_start + 1
            arr_3[i] = n2_element

    return arr_3


if __name__ == '__main__':
    print(merge_two_sorted_array([1, 3, 4, 5], 4, [2, 4, 6, 8], 4))
    print(merge_two_sorted_array([5, 8, 9, 18, 19], 5, [4, 7, 8, 12, 20, 25, 26, 28], 8))
