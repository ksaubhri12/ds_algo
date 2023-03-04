def min_swap_bracket_balance(input_value: str):
    input_string = list(input_value)
    opening_brackets_index_queue = []
    n = len(input_string)
    for i in range(0, n):
        element = input_string[i]
        if element == '[':
            opening_brackets_index_queue.append(i)
    answer = 0
    count = 0
    for i in range(0, n):
        element = input_string[i]
        if element == '[':
            count = count + 1
            opening_brackets_index_queue.pop(0)
        else:
            count = count - 1
            if count < 0:
                opening_bracket_index = opening_brackets_index_queue.pop(0)
                answer = answer + opening_bracket_index - i
                input_string[i], input_string[opening_bracket_index] = input_string[opening_bracket_index], \
                                                                       input_string[i]
                count = 1

    return answer


def min_swap_v2(input_string):
    open_bracket_count = 0
    close_bracket_count = 0
    answer = 0
    fault = close_bracket_count - open_bracket_count
    n = len(input_string)
    for i in range(0, n):
        element = input_string[i]
        if element == ']':
            close_bracket_count = close_bracket_count + 1
            fault = close_bracket_count - open_bracket_count

        else:
            open_bracket_count = open_bracket_count + 1
            if fault > 0:
                answer = answer + fault
                fault = fault - 1

    return answer


if __name__ == '__main__':
    print(min_swap_bracket_balance('[]][]['))
    print(min_swap_v2('[]][]['))
