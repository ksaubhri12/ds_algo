def longest_common_substring(string_1, string_2):
    len_1 = len(string_1)  # no of columns
    len_2 = len(string_2)  # no of rows

    dp_arr = [[0 for _ in range(len_1 + 1)] for _ in range(len_2 + 1)]
    for row_index in range(1, len_2):
        for col_index in range(1, len_1):
            if string_1[col_index] == string_2[row_index]:
                dp_arr[row_index][col_index] = 1 + dp_arr[row_index - 1][col_index - 1]
            else:
                dp_arr[row_index][col_index] = 0

    longest = float("-inf")
    for row_index in range(len_2 + 1):
        for col_index in range(len_1 + 1):
            longest = max(longest, dp_arr[row_index][col_index])

    return longest


if __name__ == '__main__':
    print(longest_common_substring("abcdef", "fgabcgh"))
