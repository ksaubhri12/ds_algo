class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.data)
            self.printInorder(root.right)

    def printPostOrder(self, root):
        if root:
            self.printPostOrder(root.left)
            self.printPostOrder(root.right)
            print(root.data)

    def printPreOrder(self, root):
        if root:
            print(root.data)
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)

    def inorderWithoutRecursions(self, root):
        stack = []
        curr = root
        self.pushLeftToStack(curr, stack)
        item = None

        while len(stack):
            item = stack.pop()
            print(item.data)
            rightItem = item.right
            if rightItem is not None and item != root:
                stack.append(rightItem)
        self.pushLeftToStack(item.right, stack)
        while len(stack):
            item = stack.pop()
            print(item.data)
            rightItem = item.right
            if rightItem is not None:
                stack.append(rightItem)

    def predecessorAndSuccessorSum(self, root):
        arr = []
        arr.append(0)
        self.inOrderPredecessorAndSuccessor(root, arr)
        arr.append(0)
        i = [1]
        self.replaceSumInorderPredecessorAndSuccessor(root, arr, i)
        root.printInorder(root)

    def inOrderPredecessorAndSuccessor(self, root, arr):
        if root:
            self.inOrderPredecessorAndSuccessor(root.left, arr)
            arr.append(root.data)
            self.inOrderPredecessorAndSuccessor(root.right, arr)

    def replaceSumInorderPredecessorAndSuccessor(self, root, arr, i):
        if root:
            self.replaceSumInorderPredecessorAndSuccessor(root.left, arr, i)
            root.data = arr[i[0] - 1] + arr[i[0] + 1]
            i[0] += 1
            self.replaceSumInorderPredecessorAndSuccessor(root.right, arr, i)

    def pushLeftToStack(self, root, stack):
        while root is not None:
            stack.append(root)
            root = root.left

    def nthNodeInInorderTraversal(self, root, n):
        i = [1]
        self.nthNodeInorderTraversalUtil(root, i, n)

    def nthNodeInorderTraversalUtil(self, root, i, n):
        if root:
            self.nthNodeInorderTraversalUtil(root.left, i, n)
            if i[0] == n:
                print(root.data)
            i[0] += 1
            self.nthNodeInorderTraversalUtil(root.right, i, n)

    def levelOrderTreeTraversal(self, root):
        queue = []
        print(root.data)
        queue.insert(0, root.left)
        queue.insert(0, root.right)

        while len(queue):
            item = queue.pop()
            print(item.data)
            if item.left:
                queue.insert(0,item.left)
            if item.right:
                queue.insert(0,item.right)

    def printLeafNodes(self,root):
        if root is None:
            return
        if root.left is None and root.right is None:
            print(root.data)
            return
        if root.right is None:
            self.printLeafNodes(root.left)
        elif root.left is None:
            self.printLeafNodes(root.right)
        else:
            self.printLeafNodes(root.left)
            self.printLeafNodes(root.right)


def buildTree(preOrderArr, inOrderArr, start, end):
    if start > end:
        return None

    tNode = Node(preOrderArr[buildTree.preIndex])
    buildTree.preIndex += 1

    if start == end:
        return tNode

    rootIndex = search(inOrderArr, start, end, tNode.data)

    tNode.left = buildTree(preOrderArr, inOrderArr, start, rootIndex - 1)
    tNode.right = buildTree(preOrderArr, inOrderArr, rootIndex + 1, end)

    return tNode


def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

buildTree.preIndex = 0
root = buildTree(preOrder,inOrder,0,len(inOrder)-1)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.left.left = Node(4)
# root.left.right = Node(5)
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.left.left.right = Node(18)

root.right.right = Node(25)
root.right.right.left = Node(20)

# root.printInorder(root)
# root.inorderWithoutRecursions(root)
# root.predecessorAndSuccessorSum(root)
# root.printPostOrder(root)
# root.printPreOrder(root)
# root.nthNodeInInorderTraversal(root, 3)
# root.levelOrderTreeTraversal(root)
root.printLeafNodes(root)