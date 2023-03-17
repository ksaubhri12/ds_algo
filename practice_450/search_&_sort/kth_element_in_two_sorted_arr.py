def kth_element_two_sorted_arr(arr_1: [], arr_2: [], n, m, k):
    i = 0
    j = 0
    count = 0
    answer = None
    while count < k:
        count = count + 1
        if i >= n:
            answer = arr_2[j]
            j = j + 1
            continue

        if j >= m:
            answer = arr_1[i]
            i = i + 1
            continue

        element_1 = arr_1[i]
        element_2 = arr_2[j]
        if element_1 < element_2:
            i = i + 1
            answer = element_1
        else:
            j = j + 1
            answer = element_2

    return answer


if __name__ == '__main__':
    print(kth_element_two_sorted_arr([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 5, 7, 7))
    print(kth_element_two_sorted_arr([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, 5))
