class Node:

    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.data)
            self.printInorder(root.right)

    def constructBinaryTree(self, pre, preLn):
        index = [0]

        return self.constructBinaryTreeUtil(pre, preLn, index)

    def constructBinaryTreeUtil(self, pre, preLn, index_ptr):
        index = index_ptr[0]
        if index == len(preLn):
            return None

        temp = Node(pre[index])
        index_ptr[0] += 1
        if preLn[index] == "N":
            temp.left = self.constructBinaryTreeUtil(pre, preLn, index_ptr)
            temp.right = self.constructBinaryTreeUtil(pre, preLn, index_ptr)

        return temp


pre = [10, 30, 20, 5, 15]
preLN = ['N', 'N', 'L', 'L', 'L']

node = Node()
root  = node.constructBinaryTree(pre,preLN)
node.printInorder(root)