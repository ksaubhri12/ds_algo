class SpecialStack:
    def __init__(self):
        self.queue_one = []
        self.queue_two = []

    def push(self, x):

        if len(self.queue_one) > 0:
            self.queue_one.append(x)
        elif len(self.queue_two) > 0:
            self.queue_two.append(x)
        else:
            self.queue_one.append(x)

    def pop(self):
        if len(self.queue_one) > 0:
            giving_queue = self.queue_one
            receiving_queue = self.queue_two

        else:
            giving_queue = self.queue_two
            receiving_queue = self.queue_one

        if len(giving_queue) == 0:
            return -1

        while len(giving_queue) > 1:
            receiving_queue.append(giving_queue.pop(0))

        print(giving_queue.pop())


if __name__ == '__main__':
    stack = SpecialStack()
    stack.push(2)

    stack.push(3)
    stack.pop()
    stack.push(4)
    stack.pop()
