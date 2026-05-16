def number_of_longest_subsequence(arr: []) -> int:
    n = len(arr)
    dp_arr = [1 for _ in range(n)]
    count_arr = [1 for _ in range(n)]
    count_arr[0] = 1
    max_len = dp_arr[0]

    for curr in range(1, n):
        for prev in range(curr):
            if arr[curr] > arr[prev] and dp_arr[curr] < 1 + dp_arr[prev]:
                dp_arr[curr] = 1 + dp_arr[prev]
                count_arr[curr] = count_arr[prev]

            elif arr[curr] > arr[prev] and dp_arr[curr] == 1 + dp_arr[prev]:
                count_arr[curr] = count_arr[curr] + count_arr[prev]

        max_len = max(max_len, dp_arr[curr])

    total = 0

    for i in range(n):
        if dp_arr[i] == max_len:
            total = total + count_arr[i]
    return total


if __name__ == '__main__':
    print(number_of_longest_subsequence([1, 3, 5, 4, 7]))
    print(number_of_longest_subsequence([2, 2, 2, 2, 2]))
