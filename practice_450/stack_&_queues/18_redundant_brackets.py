operator_map = {'+', '*', '-', '/'}


def redundant_brackets(input_str: str):
    data_stack = []
    for char in input_str:
        if char == ')':
            top_element = data_stack.pop(-1)
            if top_element == '(':
                return True

            flag = True
            while top_element != '(':
                if top_element in operator_map:
                    flag = False
                top_element = data_stack.pop(-1)

            if flag:
                return True

        else:
            data_stack.append(char)

    return False


if __name__ == '__main__':
    print(redundant_brackets('((a+b)*(c+d))'))
    print(redundant_brackets('(a+b)'))
    print(redundant_brackets('((a+b))'))

