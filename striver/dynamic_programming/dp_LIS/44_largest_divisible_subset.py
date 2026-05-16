"""
Each pair in the subset should be divisible
you can sort the array as it is about the subset and after that it becomes
longest divisible subsequence
"""


def longest_divisible_subset(arr: []):
    sorted_arr = sorted(arr)
    return longest_divisible_subsequence_tab(sorted_arr)


def longest_divisible_subsequence_tab(arr: []) -> []:
    n = len(arr)
    dp_arr = [1 for _ in range(n)]
    hash_arr = [i for i in range(n)]
    maxi_index = 0
    max_element = dp_arr[0]
    for curr in range(1, n):

        for prev in range(curr):
            if arr[curr] % arr[prev] == 0 and 1 + dp_arr[prev] > dp_arr[curr]:
                dp_arr[curr] = 1 + dp_arr[prev]
                hash_arr[curr] = prev

        if dp_arr[curr] > max_element:
            max_element = dp_arr[curr]
            maxi_index = curr

    lis_arr = [arr[maxi_index]]
    while True:
        prev_index = hash_arr[maxi_index]
        if prev_index < maxi_index:
            maxi_index = prev_index
            lis_arr.append(arr[prev_index])
        else:
            break

    return lis_arr[::-1]


if __name__ == '__main__':
    print(longest_divisible_subset([3, 4, 8, 12, 15]))
