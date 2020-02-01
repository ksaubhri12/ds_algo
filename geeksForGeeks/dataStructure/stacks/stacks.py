def createStacks():
    stack = []
    return stack


def push(stack, x):
    stack.append(x)
    return stack


def isEmpty(stack):
    return len(stack) == 0


def pop(stack):
    if isEmpty(stack):
        print("stack is empty")
    else:
        return stack.pop()
