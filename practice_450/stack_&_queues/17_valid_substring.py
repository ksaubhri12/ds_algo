def max_valid_sub_string_length(input_str: str):
    n = len(input_str)
    data_stack = [-1]
    answer = 0
    for i in range(n):
        if input_str[i] == '(':
            data_stack.append(i)
        else:
            data_stack.pop(-1)
            if len(data_stack) > 0:
                diff = i - data_stack[-1]
                answer = max(answer, diff)
            if len(data_stack) == 0:
                data_stack.append(i)

    return answer


if __name__ == '__main__':
    print(max_valid_sub_string_length(')('))
    print(max_valid_sub_string_length('(()('))
    print(max_valid_sub_string_length('()(())('))
