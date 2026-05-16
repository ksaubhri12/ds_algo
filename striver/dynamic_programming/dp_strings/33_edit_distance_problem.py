def minimum_edit_rec(string_1, string_2, index_1, index_2, dp_arr) -> int:
    if index_1 < 0:
        return index_2 + 1

    if index_2 < 0:
        return index_1 + 1

    if dp_arr[index_1][index_2] != -1:
        return dp_arr[index_1][index_2]

    if string_1[index_1] == string_2[index_2]:
        dp_arr[index_1][index_2] = minimum_edit_rec(string_1, string_2, index_1 - 1, index_2 - 1, dp_arr)
        return dp_arr[index_1][index_2]
    else:
        insert = 1 + minimum_edit_rec(string_1, string_2, index_1, index_2 - 1, dp_arr)
        delete = 1 + minimum_edit_rec(string_1, string_2, index_1 - 1, index_2, dp_arr)
        replace = 1 + minimum_edit_rec(string_1, string_2, index_1 - 1, index_2 - 1, dp_arr)
        dp_arr[index_1][index_2] = min(insert, delete, replace)
        return dp_arr[index_1][index_2]


def min_edit(string_1, string_2) -> int:
    dp_arr = [[-1 for _ in range(len(string_2))] for _ in range(len(string_1))]
    return minimum_edit_rec(string_1, string_2, len(string_1) - 1, len(string_2) - 1, dp_arr)


def min_edit_tab(source_string, target_string) -> int:
    source_len = len(source_string)  # no of columns
    target_len = len(target_string)  # no of rows
    dp_arr = [[0 for _ in range(source_len + 1)] for _ in range(target_len + 1)]
    for row_index in range(target_len + 1):
        dp_arr[row_index][0] = row_index
    for col_index in range(source_len + 1):
        dp_arr[0][col_index] = col_index

    for row_index in range(1, target_len + 1):
        for col_index in range(1, source_len + 1):
            if target_string[row_index - 1] == source_string[col_index - 1]:
                dp_arr[row_index][col_index] = dp_arr[row_index - 1][col_index - 1]
            else:
                dp_arr[row_index][col_index] = 1 + min(dp_arr[row_index - 1][col_index],
                                                       dp_arr[row_index - 1][col_index - 1],
                                                       dp_arr[row_index][col_index - 1])

    return dp_arr[target_len][source_len]


if __name__ == '__main__':
    print(min_edit("horse", "ros"))
    print(min_edit("geek", "gesek"))
    print(min_edit("gfg", "gfg"))
    print(min_edit("abcd", "bcfe"))
    print("tabulisation")
    print(min_edit_tab("horse", "ros"))
    print(min_edit_tab("geek", "gesek"))
    print(min_edit_tab("gfg", "gfg"))
    print(min_edit_tab("abcd", "bcfe"))
