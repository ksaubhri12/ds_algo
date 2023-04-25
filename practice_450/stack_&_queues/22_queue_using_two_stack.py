def Push(x, stack1: [], stack2: []):
    if len(stack1) > 0:
        stack1.append(x)
    elif len(stack2) > 0:
        stack2.append(x)
    else:
        stack1.append(x)


# Function to pop an element from queue by using 2 stacks.
def Pop(stack1: [], stack2: []):
    if len(stack1) > 0:
        giving_stack = stack1
        receiving_stack = stack2

    else:
        giving_stack = stack2
        receiving_stack = stack1

    if len(giving_stack) == 0:
        return -1
    while len(giving_stack) > 1:
        receiving_stack.append(giving_stack.pop(-1))

    res = giving_stack.pop(-1)
    while len(receiving_stack) > 0:
        giving_stack.append(receiving_stack.pop(-1))
    return res


if __name__ == '__main__':
    in_stack_1 = []
    in_stack_2 = []
    Push(11, in_stack_1, in_stack_2)
    Push(51, in_stack_1, in_stack_2)
    Push(26, in_stack_1, in_stack_2)
    print(Pop(in_stack_1, in_stack_2))
    Push(6, in_stack_1, in_stack_2)
    print(Pop(in_stack_1, in_stack_2))
    print(Pop(in_stack_1, in_stack_2))

    in_stack_1 = []
    in_stack_2 = []
    Push(2, in_stack_1, in_stack_2)
    Push(3, in_stack_1, in_stack_2)
    print(Pop(in_stack_1, in_stack_2))
    Push(4, in_stack_1, in_stack_2)
    print(Pop(in_stack_1, in_stack_2))

    in_stack_1 = []
    in_stack_2 = []
    Push(2, in_stack_1, in_stack_2)
    print(Pop(in_stack_1, in_stack_2))
    print(Pop(in_stack_1, in_stack_2))
    Push(4, in_stack_1, in_stack_2)
