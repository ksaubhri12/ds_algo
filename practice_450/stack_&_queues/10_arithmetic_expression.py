operator_precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2}


def get_arithmetic_evaluation(input_string: str):
    n = len(input_string)
    operand_stack = []
    operator_stack = []
    prev_integer = False
    for i in range(0, n):
        element = input_string[i]
        if is_integer(element):
            if prev_integer and len(operand_stack) > 0:
                curr_int_str = str(operand_stack.pop(-1))
                final_str_int = int(curr_int_str + element)
                operand_stack.append(final_str_int)

            else:
                operand_stack.append(int(element))
            prev_integer = True

        else:
            prev_integer = False
            if len(operator_stack) == 0:
                operator_stack.append(element)
            else:
                if element in operator_precedence_map:
                    top_element = operator_stack[-1]
                    while top_element != '(' and get_precedence(top_element) >= get_precedence(element) and len(
                            operator_stack) > 0:
                        pop_do_operation(operator_stack, operand_stack)
                        top_element = operator_stack[-1]
                    operator_stack.append(element)
                elif is_opening_bracket(element):
                    operator_stack.append(element)
                else:
                    top_element = operator_stack[-1]
                    while top_element != '(':
                        pop_do_operation(operator_stack, operand_stack)
                        top_element = operator_stack[-1]

    while len(operator_stack) > 0:
        pop_do_operation(operator_stack, operand_stack)
    return operand_stack[0]


def pop_do_operation(operator_stack, operand_stack):
    popped_operator = operator_stack.pop(-1)
    if popped_operator not in operator_precedence_map:
        return
    operand_2 = operand_stack.pop(-1)
    operand_1 = operand_stack.pop(-1)
    new_element = performOperation(operand_1, operand_2, popped_operator)
    operand_stack.append(new_element)


def get_precedence(operator: str):
    return operator_precedence_map[operator]


def performOperation(operand_1: int, operand_2: int, operator: str):
    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    else:
        return int(operand_1 / operand_2)


def is_integer(operand: str):
    return ord('0') <= ord(operand) <= ord('9')


def is_opening_bracket(operator: str):
    return operator == '('


def is_closing_bracket(operator: str):
    return operator == ')'


if __name__ == '__main__':
    print(get_arithmetic_evaluation('(5+(7-(6*(7/8))))'))
    print(get_arithmetic_evaluation('((8+3)+(4-((1*3)/2)))'))
    print(get_arithmetic_evaluation('(6+(((5/7)-3)/7))'))
    print(get_arithmetic_evaluation('(2)'))
    print(get_arithmetic_evaluation('((2+3)*(5/2))'))
    print(get_arithmetic_evaluation('(3*(5+2)*(10-7))'))
    print(get_arithmetic_evaluation('(121+(101+0))'))

