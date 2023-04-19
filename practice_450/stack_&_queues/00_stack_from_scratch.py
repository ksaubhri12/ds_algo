class Stack:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack_arr = []

    def push(self, num: int) -> None:
        self.stack_arr.append(num)

    def pop(self) -> int:
        if len(self.stack_arr) > 0:
            return self.stack_arr.pop(-1)
        else:
            return -1

    def top(self) -> int:
        if len(self.stack_arr) > 0:
            return self.stack_arr[-1]
        else:
            return -1

    def isEmpty(self) -> int:
        if len(self.stack_arr) == 0:
            return 1
        else:
            return 0

    def isFull(self) -> int:
        if len(self.stack_arr) == self.capacity:
            return 1
        else:
            return 0


if __name__ == '__main__':
    stack = Stack(2)
