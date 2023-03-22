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

    def print_circular_linked_list(self):
        flg = False
        temp = self.head
        while flg == False or temp != self.head:
            flg = True
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def get_count(self):
        count = 0
        curr = self.head
        while curr is not None:
            count = count + 1
            curr = curr.next
        return count
