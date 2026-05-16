def wildcard_matching_rec(source_string, target_string, source_index, target_index) -> int:
    if source_index < 0:
        if target_index < 0:
            return True
        else:
            return False

    if target_index < 0:
        if source_index > 0:
            non_star_char = [char for char in source_string[0:source_index + 1] if char != "*"]
            if len(non_star_char) > 0:
                return False
            else:
                return True

    if source_string[source_index] == target_string[target_index] or source_string[source_index] == "?":
        return wildcard_matching_rec(source_string, target_string, source_index - 1, target_index - 1)

    if source_string[source_index] == "*":
        return wildcard_matching_rec(source_string, target_string, source_index - 1,
                                     target_index) or wildcard_matching_rec(source_string, target_string, source_index,
                                                                            target_index - 1)

    else:
        return False


def wildcard_match(source_string, target_string):
    return wildcard_matching_rec(source_string, target_string, len(source_string) - 1, len(target_string) - 1)


def wildcard_match_tab(source_string, target_string):
    source_len = len(source_string)  # no of columns
    target_len = len(target_string)  # no of rows

    dp_arr = [[False for _ in range(source_len + 1)] for _ in range(target_len + 1)]
    dp_arr[0][0] = True

    for source_index in range(1, source_len + 1):
        if source_string[source_index - 1] == "*":
            dp_arr[0][source_index] = True
        else:
            break

    for row_index in range(1, target_len + 1):
        for col_index in range(1, source_len + 1):
            if source_string[col_index - 1] == target_string[row_index - 1] or source_string[col_index - 1] == "?":
                dp_arr[row_index][col_index] = dp_arr[row_index - 1][col_index - 1]
            if source_string[col_index - 1] == "*":
                dp_arr[row_index][col_index] = dp_arr[row_index - 1][col_index] or dp_arr[row_index][col_index - 1]

    return dp_arr[target_len][source_len]


if __name__ == '__main__':
    print(wildcard_match("a?c*", "abcde"))
    print(wildcard_match("a*ab", "baaabab"))
    print(wildcard_match("*", "abc"))
    print("tabulisation")
    print(wildcard_match_tab("a?c*", "abcde"))
    print(wildcard_match_tab("a*ab", "baaabab"))
    print(wildcard_match_tab("*", "abc"))

