"""
when at element i, find lower bound of it in the sorted array that we are creating
The idea is to create a sorted array while traversing the array and updating adding the element based on the
lower bound, that is how you will get your longest increasing sub sequence
"""


def lower_bound(arr, start_index, end_index, element):
    """
    index of `element` in arr or index of first element in the arr that is > element
    """
    if start_index >= end_index:
        return start_index

    mid_index = start_index + (end_index - start_index) // 2

    if arr[mid_index] < element:
        return lower_bound(arr, mid_index + 1, end_index, element)
    else:
        return lower_bound(arr, start_index, mid_index, element)


def lis_length(arr: []) -> int:
    n = len(arr)
    sorted_array = [arr[0]]
    for i in range(1, n):
        new_element = arr[i]
        if new_element > sorted_array[-1]:
            sorted_array.append(new_element)
        else:
            index_to_replace = lower_bound(sorted_array, 0, len(sorted_array) - 1, new_element)
            sorted_array[index_to_replace] = new_element

    return len(sorted_array)


if __name__ == '__main__':
    print(lis_length([3, 10, 2, 1, 20]))
    print(lis_length([30, 20, 10]))
    print(lis_length([2, 2, 2]))
    print(lis_length([3, 4, 5, 1, 2, 3, 4]))
