def longest_string_chain_tab(arr: []) -> []:
    n = len(arr)
    arr = sorted(arr)
    dp_arr = [1 for _ in range(n)]
    hash_arr = [i for i in range(n)]
    max_element = dp_arr[0]
    for curr in range(1, n):

        for prev in range(curr):
            if compare(arr[curr], arr[prev]) and 1 + dp_arr[prev] > dp_arr[curr]:
                dp_arr[curr] = 1 + dp_arr[prev]
                hash_arr[curr] = prev

        if dp_arr[curr] > max_element:
            max_element = dp_arr[curr]

    return max_element


def compare(string_1, string_2) -> bool:
    string_1_len = len(string_1)
    if len(string_1) - len(string_2) != 1:
        return False

    i = 0
    j = 0

    while i < string_1_len and j < len(string_2):
        if string_1[i] == string_2[j]:
            i = i + 1
            j = j + 1
            continue
        else:
            i = i + 1

    return i == len(string_1) and j == len(string_2)


if __name__ == '__main__':
    print(compare("abcs", "bcs"))
    print(compare("absc", "bcs"))
    print(compare("dasc", "dsc"))
    print(compare("ba", "b"))

    print(longest_string_chain_tab(["ba", "b", "a", "bca", "bda", "bdca"]))
