from collections import deque


class Stack:
    def __init__(self):
        self.data = deque()

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()

        else:
            return -1


class Queue:
    def __init__(self):
        self.data = deque()

    def push(self, x):
        self.data.appendleft(x)

    def pop(self):
        if len(self.data) > 0:
            self.data.popleft()
        return -1
