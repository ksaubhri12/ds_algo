# The idea is to use binary search to see how many elements are common
# Once you get the common element rest of the element is your union length

def binary_search(arr: [], start: int, end: int, k):
    if start >= end and arr[start] == k:
        return start

    if start >= end and arr[start] != k:
        return -1

    middle_index = int((start + end) / 2)

    middle_element = arr[middle_index]

    if middle_element < k:
        return binary_search(arr, middle_index + 1, end, k)
    else:
        return binary_search(arr, start, middle_index, k)


def intersection_two_array(arr1: [], n, arr2: [], m):
    count = 0
    for i in range(0, n):
        element_to_find = arr1[i]
        element_index_in_other_array = binary_search(arr2, 0, m - 1, element_to_find)
        if element_index_in_other_array != -1:
            count = count + 1

    return count


def union_two_array(arr1: [], n, arr2: [], m):
    common_element = intersection_two_array(arr1, n, arr2, m)
    total_element = n + m
    return total_element - common_element


def union_two_array_v2(arr1: [], n, arr2: [], m):
    final_dict = {}
    for i in range(0, n):
        element = arr1[i]
        final_dict[element] = 1
    for i in range(0, m):
        element = arr2[i]
        final_dict[element] = 1

    return len(final_dict.keys())


if __name__ == '__main__':
    # print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 78, 90, 100], 0, 14, 91))

    print(union_two_array_v2([1, 2, 3, 4, 5], 5, [1, 2, 3], 3))
