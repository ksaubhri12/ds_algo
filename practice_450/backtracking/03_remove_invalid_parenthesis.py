def remove_parenthesis(input_string):
    n = len(input_string)
    result_arr = {}
    string_map = {}
    min_count = get_min_count(input_string, n)
    get_all_strings(input_string, min_count, result_arr, n, string_map)
    return list(result_arr.keys())


def get_min_count(input_string: str, n: int):
    bracket_stack = []
    for i in range(0, n):
        char = input_string[i]
        if char == '(':
            bracket_stack.append(char)
        elif char == ')':
            if len(bracket_stack) > 0:
                element_pop = bracket_stack.pop()
                if element_pop == '(':
                    continue
                else:
                    bracket_stack.append(element_pop)
                    bracket_stack.append(char)
            else:
                bracket_stack.append(char)

    return len(bracket_stack)


def get_all_strings(input_string, min_invalid, result_arr: [], n, string_map: {}):
    if input_string in string_map:
        return

    string_map[input_string] = 1

    if min_invalid < 0:
        return
    if min_invalid == 0:
        if get_min_count(input_string, n) == 0:
            result_arr[input_string] = 1
        return

    for i in range(0, n):
        left_piece = input_string[:i]
        right_piece = input_string[i + 1:]
        get_all_strings(left_piece + right_piece, min_invalid - 1, result_arr, n - 1, string_map)

    return


if __name__ == '__main__':
    print(remove_parenthesis('((()((s((((()'))
    print(remove_parenthesis('()())()'))
    print(remove_parenthesis('(a)())()'))
