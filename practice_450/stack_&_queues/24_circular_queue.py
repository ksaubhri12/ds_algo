class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self, n):
        self.capacity = n
        self.size = 0
        self.head = None
        self.end = None

    def enqueue(self, value):
        if self.size == self.capacity:
            return False
        self.size = self.size + 1
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.end = new_node

            return True

        else:
            new_node = Node(value)
            curr_end = self.end
            self.end = new_node
            curr_end.next = new_node
            return True

    def deque(self):
        if self.size == 0:
            return -1
        self.size = self.size - 1
        curr_head = self.head
        self.head = curr_head.next
        return curr_head.data

