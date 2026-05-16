"""
This is nothing but we need to view LIS from front and back
then the sum of these two dp array at each index
whichever is the max minus the 1 because of the common element
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


def lis_length(arr: []) -> []:
    n = len(arr)
    sorted_array = [arr[0]]
    dp_arr = [1]
    for i in range(1, n):
        new_element = arr[i]
        if new_element > sorted_array[-1]:
            sorted_array.append(new_element)
        else:
            index_to_replace = lower_bound(sorted_array, 0, len(sorted_array) - 1, new_element)
            sorted_array[index_to_replace] = new_element
        dp_arr.append(len(sorted_array))

    return dp_arr


def is_sorted(arr):
    increasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    decreasing = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    return increasing or decreasing


def longest_bitonic_subsequence(arr):
    if is_sorted(arr):
        return 0
    n = len(arr)
    # front_lis_arr = lis_length(arr)
    # reversed_lis_arr = lis_length(arr[::-1])
    # reversed_lis_arr = reversed_lis_arr[::-1]

    front_lis_arr_tab = lis_tab(arr)
    reversed_lis_arr_tab = lis_tab(arr[::-1])
    reversed_lis_arr_tab = reversed_lis_arr_tab[::-1]

    maxi = front_lis_arr_tab[0] + reversed_lis_arr_tab[0]
    for i in range(1, n):
        maxi = max(maxi, front_lis_arr_tab[i] + reversed_lis_arr_tab[i])

    return maxi - 1


def lis_tab(arr) -> []:
    n = len(arr)
    dp_arr = [1 for _ in range(n)]
    for curr in range(1, n):
        for prev in range(curr):
            if arr[curr] > arr[prev] and dp_arr[curr] < 1 + dp_arr[prev]:
                dp_arr[curr] = 1 + dp_arr[prev]
    return dp_arr


if __name__ == '__main__':
    print(longest_bitonic_subsequence([1, 4, 2, 7, 9, 10]))
    # print(longest_bitonic_subsequence([5, 7, 9]))
    # print(longest_bitonic_subsequence([1, 2, 5, 3, 2]))
    # print(longest_bitonic_subsequence([1, 11, 2, 10, 4, 5, 2, 1]))
    # print(longest_bitonic_subsequence([10, 20, 30]))
