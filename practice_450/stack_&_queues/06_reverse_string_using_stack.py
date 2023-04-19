


def reverse_string(input_string):
    input_stack = []
    for char in input_string:
        input_stack.append(char)

    final_string = ''
    while len(input_stack) > 0:
        final_string = final_string + input_stack.pop(-1)

    return final_string


if __name__ == '__main__':
    print(reverse_string('suna'))
