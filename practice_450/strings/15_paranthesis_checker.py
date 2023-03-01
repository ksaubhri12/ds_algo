def parenthesis_checker(string_value: str):
    opening_brackets = {'[': ']', '(': ')', '{': '}'}

    opening_brackets_stack = []

    answers = True
    n = len(string_value)
    for i in range(0, n):
        element = string_value[i]
        if element in opening_brackets:
            opening_brackets_stack.append(element)
        else:
            if len(opening_brackets_stack) > 0:
                element_in_stack = opening_brackets_stack.pop()
                if not check_pair(element_in_stack, element):
                    answers = False
                    break
            else:
                answers = False
                break

    if answers and len(opening_brackets_stack) == 0:
        return 'balanced'
    else:
        return 'not balanced'


def check_pair(opening_element, closing_element):
    opening_brackets = {'[': ']', '(': ')', '{': '}'}
    return closing_element == opening_brackets[opening_element]


if __name__ == '__main__':
    print(parenthesis_checker('[()]{}{[()()]()}'))
    print(parenthesis_checker(' [(])'))
    print(parenthesis_checker('('))
