class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class StackMiddleElement:
    def __init__(self):
        self.head = None
        self.end = None
        self.middle = None
        self.size = 0

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.end = self.head
            self.middle = self.head
            self.size = self.size + 1
        else:
            new_node = Node(data)
            curr_end = self.end
            self.end = new_node
            curr_end.next = new_node
            new_node.prev = curr_end
            self.size = self.size + 1
            if self.size % 2 != 0:
                self.middle = self.middle.next

    def pop(self):
        end_node = self.end
        prev_node = end_node.prev
        self.end = prev_node
        self.end.next = None
        self.size = self.size - 1
        if self.size % 2 == 0:
            self.middle = self.middle.prev

    def find_middle(self):
        return self.middle.data

    def delete_middle(self):
        curr_middle = self.middle
        prev_node = curr_middle.prev
        next_node = curr_middle.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size = self.size - 1
        if self.size % 2 == 0:
            self.middle = prev_node
        else:
            self.middle = next_node

    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next
        print()


if __name__ == '__main__':
    stack = StackMiddleElement()
    print('Add 1')
    stack.push(1)
    stack.print()
    print('Add 2, 3, 4, 5, 6, 7')
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.print()
    print('Find Middle')
    print(stack.find_middle())
    print('Add 8')
    stack.push(8)
    stack.print()
    print('Find Middle')
    print(stack.find_middle())
    print('Remove Middle')
    stack.delete_middle()
    print('Current Stack ')
    stack.print()
    print('Current Middle')
    print(stack.find_middle())
    print('Pop')
    stack.pop()

    print('Current Stack')
    stack.print()
    print('Middle Element')
    print(stack.find_middle())
