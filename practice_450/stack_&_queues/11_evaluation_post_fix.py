def post_fix_evaluation(input_string):
    operand_stack = []
    n = len(input_string)
    for i in range(n):
        element = input_string[i]
        if is_integer(element):
            operand_stack.append(int(element))
        else:
            pop_do_operation(operand_stack, element)

    return operand_stack[0]


def performOperation(operand_1: int, operand_2: int, operator: str):
    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    else:
        return int(operand_1 / operand_2)


def pop_do_operation(operand_stack: [], operator: str):
    operand_2 = operand_stack.pop(-1)
    operand_1 = operand_stack.pop(-1)
    new_element = performOperation(operand_1, operand_2, operator)
    operand_stack.append(new_element)


def is_integer(element):
    return ord('0') <= ord(element) <= ord('9')


if __name__ == '__main__':
    print(post_fix_evaluation('231*+9-'))
    print(post_fix_evaluation('123+*8-'))
