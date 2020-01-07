class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def append(self, newValue):
        newNode = Node(newValue)

        if self.head is None:
            self.head = newNode
            return
        currNode = self.head
        while currNode.next is not None:
            currNode = currNode.next
        currNode.next = newNode

    def mergeSort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.getMiddle(head)
        nextToMiddle = middle.next

        middle.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(nextToMiddle)

        head = self.merge(left, right)

        return head

    def merge(self, left, right):
        result = None
        if left is None:
            return right
        if right is None:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    @staticmethod
    def printLinkedList(head):
        if head is None:
            print(" ")
            return
        curr = head
        while curr:
            print(curr.data)
            curr = curr.next

    @staticmethod
    def getMiddle(head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
