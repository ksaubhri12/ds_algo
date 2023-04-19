class TwoStack:
    def __init__(self):
        self.tos_1 = -1
        self.tos_2 = 101


two_stack = TwoStack()


def push1(a, x):
    if two_stack.tos_2 - two_stack.tos_1 == 1:
        return

    if two_stack.tos_1 == 100:
        return
    two_stack.tos_1 = two_stack.tos_1 + 1
    a[two_stack.tos_1] = x


def push2(a, x):
    if two_stack.tos_2 - two_stack.tos_1 == 1:
        return

    if two_stack.tos_2 == 0:
        return
    two_stack.tos_2 = two_stack.tos_2 - 1
    a[two_stack.tos_2] = x


def pop1(a):
    if two_stack.tos_1 == -1:
        return -1
    result = a[two_stack.tos_1]
    a[two_stack.tos_1] = -1
    two_stack.tos_1 = two_stack.tos_1 - 1
    return result


def pop2(a):
    if two_stack.tos_2 == 101:
        return -1
    result = a[two_stack.tos_2]
    a[two_stack.tos_2] = -1
    two_stack.tos_2 = two_stack.tos_2 + 1
    return result
