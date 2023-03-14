def find_all_four_number(arr: [], k):
    arr = sorted(arr)
    n = len(arr)
    final_dict = {}
    for first in range(0, n):
        for second in range(first + 1, n):
            for third in range(second + 1, n):
                fourth_value = k - (arr[first] + arr[second] + arr[third])
                fourth_value_index = binary_search(arr, third + 1, n - 1, fourth_value)
                if fourth_value_index != -1:
                    string_key = str(arr[first]) + "_" + str(arr[second]) + "_" + str(arr[third]) + "_" + str(
                        fourth_value)
                    final_dict[string_key] = [arr[first], arr[second], arr[third], fourth_value]
    final_arr = []
    for value in final_dict.values():
        final_arr.append(value)
    return final_arr


def binary_search(arr: [], start: int, end: int, k):
    while start <= end:
        middle_index = start + (end - start) // 2
        middle_element = arr[middle_index]
        if middle_element == k:
            return middle_index
        if middle_element < k:
            start = middle_index + 1
        else:
            end = middle_index - 1

    return -1


if __name__ == '__main__':
    print(find_all_four_number(
        [88, 84, 3, 51, 54, 99, 32, 60, 76, 68, 39, 12, 26, 86, 94, 39, 95, 70, 34, 78, 67, 1, 97, 2, 17, 92, 52], 179))
    # print(find_all_four_number([0, 0, 2, 1, 1], 5, 3))
