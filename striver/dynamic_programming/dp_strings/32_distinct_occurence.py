"""
This is based on string matching
"""


def distinct_subsequence_rec(string_1, string_2, index_1, index_2) -> int:
    if index_2 < 0:
        return 1
    if index_1 < 0:
        return 0

    if string_1[index_1] == string_2[index_2]:
        return distinct_subsequence_rec(string_1, string_2, index_1 - 1, index_2 - 1) + distinct_subsequence_rec(
            string_1, string_2, index_1 - 1, index_2)
    else:
        return distinct_subsequence_rec(string_1, string_2, index_1 - 1, index_2)


def distinct_subsequence(string_1, string_2) -> int:
    return distinct_subsequence_rec(string_1, string_2, len(string_1) - 1, len(string_2) - 1)


def distinct_subsequence_tab(source, target):
    rows_len = len(target)
    col_len = len(source)
    dp_arr = [[0 for _ in range(col_len + 1)] for _ in range(rows_len + 1)]
    for row in range(rows_len + 1):
        dp_arr[row][0] = 0
    for col in range(col_len + 1):
        dp_arr[0][col] = 1

    for row in range(1, rows_len + 1):
        for col in range(1, col_len + 1):
            if target[row - 1] == source[col - 1]:
                dp_arr[row][col] = dp_arr[row - 1][col - 1] + dp_arr[row][col - 1]
            else:
                dp_arr[row][col] = dp_arr[row][col - 1]
    return dp_arr[rows_len][col_len]


if __name__ == '__main__':
    print(distinct_subsequence_tab("abba", "aba"))
    print(distinct_subsequence_tab("banana", "ban"))
