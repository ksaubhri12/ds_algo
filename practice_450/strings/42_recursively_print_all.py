def recursively_print_all_words(words_list_list: [[str]]):
    row_len = len(words_list_list)
    col_len = len(words_list_list[0])
    output = [''] * row_len
    for i in range(0, col_len):
        if words_list_list[0][i] != '':
            print_util(words_list_list, row_len, col_len, 0, i, output)


def print_util(words_list_list: [[str]], row_len, col_len, row, col, output):
    output[row] = words_list_list[row][col]

    if row == row_len - 1:
        print(' '.join([str(i) for i in output]))
        return

    for i in range(0, col_len):
        if words_list_list[row + 1][i] != '':
            print_util(words_list_list, row_len, col_len, row + 1, i, output)


if __name__ == '__main__':
    recursively_print_all_words(
        [["you", "we", ""],
         ["have", "are", ""],
         ["sleep", "eat", "drink"]])
