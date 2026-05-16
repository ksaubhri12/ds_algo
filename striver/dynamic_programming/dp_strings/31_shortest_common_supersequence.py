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
                dp_arr[row_index][column_index] = max(dp_arr[row_index - 1][column_index],
                                                      dp_arr[row_index][column_index - 1])

    return dp_arr[len_2 - 1][len_1 - 1]


def shortest_common_super_sequence(string_1: str, string_2: str) -> int:
    common_subsequence = longest_common_subsequence_tab(string_1, string_2)
    first_string_remaining = len(string_1) - common_subsequence
    second_string_remaining = len(string_2) - common_subsequence
    return first_string_remaining + second_string_remaining + common_subsequence


if __name__ == '__main__':
    print(shortest_common_super_sequence("geek", "eke"))
    print(shortest_common_super_sequence("AGGTAB", "GXTXAYB"))
    print(shortest_common_super_sequence("geek", "ek"))
