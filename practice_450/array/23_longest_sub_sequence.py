def longest_sub_sequence(arr: [], n):
    arr = sorted(arr)
    res = 1
    max_res = 1
    last_element = arr[0]
    for i in range(1, n):
        curr_element = arr[i]
        if curr_element == last_element:
            continue

        if curr_element == last_element + 1:
            res = res + 1
            last_element = curr_element
        else:
            res = 1
            last_element = curr_element

        max_res = max(res, max_res)

    return max_res


if __name__ == '__main__':
    print(longest_sub_sequence([2, 4, 6, 7, 8, 10], 6))
    print(longest_sub_sequence([2, 6, 1, 9, 4, 5, 3], 7))
    print(longest_sub_sequence([1, 9, 3, 10, 4, 20, 2], 7))
    print(longest_sub_sequence([6, 6, 2, 3, 1, 4, 1, 5, 6, 2, 8, 7, 4, 2, 1, 3, 4, 5, 9, 6], 20))
