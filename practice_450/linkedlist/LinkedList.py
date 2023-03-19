from Node import Node


class LinkedList:
    def __init__(self, head: Node):
        self.head = head

    def print_linked_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next

        print()
