brackets_pair_map = {'[': ']', '(': ')', '{': '}'}


def is_balanced(input_string: str):
    input_stack = []
    answer = True
    for char in input_string:
        if char in brackets_pair_map:
            input_stack.append(char)
        else:
            if len(input_stack) > 0:
                char_pop = input_stack.pop(-1)
                if brackets_pair_map[char_pop] != char:
                    answer = False
                    break

            else:
                answer = False
                break

    return 'balanced' if answer and len(input_stack) == 0 else 'not balanced'


if __name__ == '__main__':
    print(is_balanced('{([])}'))
    print(is_balanced('([]'))
