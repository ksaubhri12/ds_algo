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

    def insertAtFront(self, newValue):
        newNode = Node(newValue)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def lengthOfLinkedListIterative(self):
        if self.head is None:
            return 0
        count = 0
        curr = self.head
        while curr is not None:
            curr = curr.next
            count += 1
        return count

    def getCountRecursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.getCountRecursive(node.next)

    def deleteNode(self, value):
        if self.head.data == value:
            nodeToBeDeleted = self.head
            self.head = self.head.next
            nodeToBeDeleted = None
            return
        curr = self.head
        prev = None
        while curr is not None:
            if curr.data == value:
                prev.next = curr.next
                curr = None

            prev = curr
            curr = curr.next

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

    def searchLinkedListIter(self, node, x):
        if node is None:
            return False
        if node.data == x:
            return True
        return self.searchLinkedListIter(node.next, x)

    def searchLinkedListRec(self, x):
        if self.head is None:
            return False
        curr = self.head
        while curr is not None:
            if curr.data == x:
                return True
            curr = curr.next
        return False

    def getNthElement(self, index):
        if index == 0:
            return self.head
        count = 0
        curr = self.head
        while curr is not None:
            if count == index:
                return curr.data
            curr = curr.next
            count = count + 1
        return None

    def getNthElementFromLast(self, index):
        if self.head is None:
            return None
        len = self.getCountRecursive(self.head)
        return self.getNthElement(len - index + 1)

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
    def detectAndCountLoop(head):
        if head is None:
            return 0

        visitedNode = {}
        curr = head
        count = 0
        while curr is not None:
            if curr.next is not None:
                if curr.next == curr:
                    return 1
                if curr.next in visitedNode:
                    return count - visitedNode[curr.next] + 1
            visitedNode[curr] = count
            count = count + 1
            curr = curr.next
        return 0

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

    @staticmethod
    def isPalindrome(head):
        if head is None:
            return False
        visitedStack = []
        curr = head
        while curr is not None:
            visitedStack.append(curr)
            curr = curr.next
        curr = head
        length = len(visitedStack)
        for i in range(length):
            var = visitedStack.pop().data
            if var != curr.data:
                return False
            curr = curr.next
        return True

    @staticmethod
    def removeDuplicates(head):
        if head is None:
            return None
        curr = head
        while curr.next is not None:
            if curr.next.data == curr.data:
                new = curr.next.next
                curr.next = None
                curr.next = new
            else:
                curr = curr.next
        return head

    @staticmethod
    def removeDuplicateFromUnsortedLinkedList(head):
        if head is None:
            return None
        visitedNodeDict = {}
        curr = head
        while curr is not None:
            if curr.data in visitedNodeDict:
                curr = curr.next
            else:
                visitedNodeDict[curr.data] = True
                curr = curr.next
        newLinkedList = LinkedList()
        for data in visitedNodeDict:
            newLinkedList.append(data)
        return newLinkedList.head

    @staticmethod
    def swapNodes(head, key1, key2):
        if head.data == key1:
            pass
        key1PrevNode = None
        key2PrevNode = None
        curr = head
        while curr.next is not None:
            if curr.next.data == key1:
                key1PrevNode = curr
            if curr.next.data == key2:
                key2PrevNode = curr
            curr = curr.next
        if key1PrevNode is None or key2PrevNode is None:
            return head

        newKey1Node = Node(key2)
        newKey1Node.next = key1PrevNode.next.next
        key1PrevNode.next = None
        key1PrevNode.next = newKey1Node

        newKey2Node = Node(key1)
        newKey2Node.next = key2PrevNode.next.next
        key2PrevNode.next = None
        key2PrevNode.next = newKey2Node

        return head
