class ListNode:

    def __init__(self,data):
        self.data = data
        self.next = None



class BinaryTreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Conversion:

    def __init__(self):
        self.head = None
        self.root = None

    def push(self,newData):
        newNode = ListNode(newData)
        newNode.next = self.head

        self.head = newNode

    def convertListToBinaryTree(self):

        q = []
        if self.head is None:
            return  None

        self.root = BinaryTreeNode(self.head.data)
        q.append(self.root)

        self.head = self.head.next

        while self.head:
            parent = q.pop(0)

            leftChild = None
            rightChild = None

            leftChild = BinaryTreeNode(self.head.data)
            self.head = self.head.next
            q.append(leftChild)
            if self.head :
                rightChild = BinaryTreeNode(self.head.data)
                self.head = self.head.next
                q.append(rightChild)

            parent.left = leftChild
            parent.right = rightChild

    def inOrderPrint(self,root):
        if root:
            self.inOrderPrint(root.left)
            print(root.data)
            self.inOrderPrint(root.right)

    def convertArrayToBinaryList(self, arr):
        if len(arr) is None:
            return None
        q = []
        self.root = BinaryTreeNode(arr[0])
        q.append(self.root)
        i = 1
        while i < len(arr):
            parent = q.pop(0)
            leftChild = None
            rightChild = None

            leftChild = BinaryTreeNode(arr[i])
            i += 1
            q.append(leftChild)
            if i < len(arr):
                rightChild = BinaryTreeNode(arr[i])
                i += 1
                q.append(rightChild)
            parent.left = leftChild
            parent.right = rightChild



conv = Conversion()
conv.push(36)
conv.push(30)
conv.push(25)
conv.push(15)
conv.push(12)
conv.push(10)

conv.convertListToBinaryTree()

conv.inOrderPrint(conv.root)
conv.convertArrayToBinaryList([1,2,3,4,5,6])
conv.inOrderPrint(conv.root)


