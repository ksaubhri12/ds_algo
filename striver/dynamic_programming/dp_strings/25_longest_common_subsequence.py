def longest_common_subsequence_rec(string_1, string_2, index_1, index_2):
    if index_1 < 0 or index_2 < 0:
        return 0

    if string_1[index_1] == string_2[index_2]:
        return 1 + longest_common_subsequence_rec(string_1, string_2, index_1 - 1, index_2 - 1)

    combinations = [[0, 1], [1, 0], [1, 1]]
    longest = float("-inf")
    for combination in combinations:
        len = longest_common_subsequence_rec(string_1, string_2, index_1 - combination[0], index_2 - combination[1])
        longest = max(len, longest)
    return longest


def longest_common_subsequence(string_1, string_2):
    index_1 = len(string_1) - 1
    index_2 = len(string_2) - 1
    return longest_common_subsequence_rec(string_1, string_2, index_1, index_2)


def longest_common_subsequence_tab(string_1, string_2):
    len_1 = len(string_1)  # no of columns
    len_2 = len(string_2)  # no of rows
    dp_arr = [[0 for _ in range(len_1)] for _ in range(len_2)]
    char_to_match = string_1[0]
    found = False
    for i in range(len_2):
        curr_char = string_2[i]
        if found:
            dp_arr[i][0] = 1
        else:
            if curr_char == char_to_match:
                found = True
                dp_arr[i][0] = 1

    found = False
    char_to_match = string_2[0]

    for i in range(len_1):
        curr_char = string_1[i]
        if found:
            dp_arr[0][i] = 1
        else:
            if curr_char == char_to_match:
                found = True
                dp_arr[0][i] = 1

    for row_index in range(1, len_2):
        for column_index in range(1, len_1):
            if string_2[row_index] == string_1[column_index]:
                dp_arr[row_index][column_index] = 1 + dp_arr[row_index - 1][column_index - 1]
            else:
                dp_arr[row_index][column_index] = max(dp_arr[row_index-1][column_index], dp_arr[row_index][column_index-1])

    return dp_arr[len_2 - 1][len_1 - 1]


if __name__ == '__main__':
    print(longest_common_subsequence_tab("abcd", "acfed"))
    print(longest_common_subsequence_tab("ABCDGH", "AEDFHR"))
    print(longest_common_subsequence_tab("ABC", "AC"))
    print(longest_common_subsequence_tab("XYZW", "XYWZ"))
