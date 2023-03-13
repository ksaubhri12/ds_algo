def search(nums: [int], target: int):
    return search_rotated_sorted_arr(nums, 0, len(nums) - 1, target)


def search_rotated_sorted_arr(arr: [], start: int, end: int, k):
    if start > end:
        return -1

    middle_index = start + (end - start) // 2
    middle_element = arr[middle_index]
    if middle_element == k:
        return middle_index

    if arr[start] <= middle_element:  # Left Part is Sorted
        if arr[start] <= k < middle_element:  # Left Part is Sorted and element lies in middle.
            return binary_search(arr, start, middle_index, k)

        else:
            return search_rotated_sorted_arr(arr, middle_index + 1, end, k)  # Search in right side of the array
    else:  # right part is sorted for sure
        if middle_element < k <= arr[end]:
            return binary_search(arr, middle_index + 1, end, k)
        else:
            return search_rotated_sorted_arr(arr, start, middle_index - 1, k)


def binary_search(arr: [], start: int, end: int, k):
    if start > end:
        return -1

    middle_index = start + (end - start) // 2
    middle_element = arr[middle_index]
    if middle_element == k:
        return middle_index
    if middle_element < k:
        return binary_search(arr, middle_index + 1, end, k)
    else:
        return binary_search(arr, start, middle_index - 1, k)


if __name__ == '__main__':
    print(search([5, 1, 3], 5))
    print(search_rotated_sorted_arr([0, 1, 2, 4, 4, 5, 6, 7], 0, 7, 4))
    print(search_rotated_sorted_arr([4, 5, 6, 7, 0, 1, 2], 0, 6, 0))
    print(search_rotated_sorted_arr([4, 5, 6, 7, 0, 1, 2], 0, 6, 3))
    print(search_rotated_sorted_arr([1], 0, 0, 0))
    print(search_rotated_sorted_arr([1], 0, 0, 1))
    print(search([3, 1], 1))
