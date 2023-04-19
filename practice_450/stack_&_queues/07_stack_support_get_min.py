class SpecialStack:
    def __init__(self):
        self.stack = []
        self.min_element = None

    def push(self, data):
        if len(self.stack) == 0:
            self.stack.append(data)
            self.min_element = data
            return

        if self.min_element <= data:
            self.stack.append(data)
            return

        else:
            value = 2 * data - self.min_element
            self.min_element = data
            self.stack.append(value)

    def get_min(self):
        return self.min_element

    def pop(self):
        popped_element = self.stack.pop(-1)
        if popped_element >= self.min_element:
            return popped_element
        else:
            self.min_element = 2 * self.min_element - popped_element
            data = (popped_element + self.min_element) // 2
            return data


if __name__ == '__main__':
    stack = SpecialStack()
    stack.push(10)
    stack.push(9)
    stack.push(8)
    stack.push(7)

    print(stack.get_min())
    print(stack.pop())
    print(stack.get_min())