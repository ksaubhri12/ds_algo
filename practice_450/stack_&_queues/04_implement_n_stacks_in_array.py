class SpecialStacks:
    def __init__(self, n, k):
        self.data_arr = [None] * n
        self.free = 0
        self.next = [(i + 1) for i in range(n)]
        self.next[n - 1] = -1
        self.top = [-1] * k

    def is_full(self):
        return self.free == -1

    def is_empty(self, stack_number):
        return self.top[stack_number] == -1

    def push(self, stack_number, item):
        if self.is_full():
            print('Stack Overflow')
            return

        insert_at = self.free
        self.data_arr[insert_at] = item

        self.free = self.next[insert_at]
        self.next[insert_at] = self.top[stack_number]
        self.top[stack_number] = insert_at

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            return None

        top_of_stack = self.top[stack_number]

        self.top[stack_number] = self.next[top_of_stack]
        self.next[top_of_stack] = self.free
        self.free = top_of_stack

        return self.data_arr[top_of_stack]

