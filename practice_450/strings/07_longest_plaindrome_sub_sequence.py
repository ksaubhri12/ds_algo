def longest_palindrome(string: str, start, end):
    if start > end:
        return [0, end, start]

    extent_range = check_string_is_palindrome_to_which_extent(string, start, end)
    extent_range_start = extent_range[0]
    extent_range_end = extent_range[1]

    if extent_range_end - extent_range_start <= 1:
        return [end - start, end, start]

    if extent_range_start == start:
        extent_range_start = start + 1
    if extent_range_end == end:
        extent_range_end = end - 1

    # if extent_range_end - extent_range_start == 1:
    #     return [end - start, start, end]
    range_1_value = longest_palindrome(string, start, extent_range_end)
    range_2_value = longest_palindrome(string, extent_range_start, end)
    range_1 = range_1_value[0]
    range_2 = range_2_value[0]
    if range_1 > range_2:
        final_range = range_1_value
    else:
        final_range = range_2_value

    range_end = final_range[1]
    range_start = final_range[2]
    return [range_end - range_start, range_end, range_start]


def longest_palindrome_driver(string: str):
    n = len(string)
    value = longest_palindrome(string, 0, n - 1)
    return string[value[2]:value[1] + 1]


def check_string_is_palindrome_to_which_extent(string, start: int, end: int):
    while start <= end:
        if string[start] != string[end]:
            return [start, end]
        start = start + 1
        end = end - 1

    return [start, end]


if __name__ == '__main__':
    # print(longest_palindrome_driver('aaaabbaa'))
    print(longest_palindrome_driver('abc'))
