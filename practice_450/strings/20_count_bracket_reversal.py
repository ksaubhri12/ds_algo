def count_brackets_reversal(input_string):
    n = len(input_string)
    if n % 2 != 0:
        return -1

    brackets_pair = {'[': ']', '(': ')', '{': '}'}
    output_stacks = []
    non_pair_closing_count = 0
    for i in range(0, n):
        element = input_string[i]
        if element in brackets_pair:
            output_stacks.append(element)
        else:
            if len(output_stacks) > 0:
                element_from_output_stack = output_stacks.pop()
                if not check_pair(element_from_output_stack, element):
                    output_stacks.append(element_from_output_stack)
                    non_pair_closing_count = non_pair_closing_count + 1
            else:
                non_pair_closing_count = non_pair_closing_count + 1

    open_brackets_count = len(output_stacks)
    closing_brackets_count = non_pair_closing_count
    single_flip = open_brackets_count // 2 + closing_brackets_count // 2
    dual_flip = open_brackets_count % 2 + closing_brackets_count % 2

    return single_flip + dual_flip


def check_pair(opening_element, closing_element):
    opening_brackets = {'[': ']', '(': ')', '{': '}'}
    return closing_element == opening_brackets[opening_element]


if __name__ == '__main__':
    print(count_brackets_reversal('}{{}}{{{'))
    print(count_brackets_reversal('{{}{{{}{{}}{{'))
    print(count_brackets_reversal('}{}{}{}}}{{{{{}{}{}}{{}{}{}}{{}}{{'))

