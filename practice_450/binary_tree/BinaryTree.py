from Node import Node


class BinaryTree:
    def __init__(self, node: Node):
        self.root = node

    def in_order_traversal(self):
        result_arr = []
        BinaryTree.in_order_traversal_util(self.root, result_arr)
        for val in result_arr:
            print(val, end=' ')
        print()

    def pre_order(self):
        result_arr = []
        BinaryTree.pre_order_util(self.root, result_arr)
        for val in result_arr:
            print(val, end=' ')
        print()

    def post_order(self):
        result_arr = []
        BinaryTree.post_order_util(self.root, result_arr)
        for val in result_arr:
            print(val, end=' ')
        print()

    @staticmethod
    def pre_order_util(root, result_arr):
        if root is None:
            return
        result_arr.append(root.data)
        BinaryTree.pre_order_util(root.left, result_arr)
        BinaryTree.pre_order_util(root.right, result_arr)

    @staticmethod
    def in_order_traversal_util(root, result_arr: []):
        if root is None:
            return

        BinaryTree.in_order_traversal_util(root.left, result_arr)
        result_arr.append(root.data)
        BinaryTree.in_order_traversal_util(root.right, result_arr)

    @staticmethod
    def post_order_util(root, result_arr: []):
        if root is None:
            return
        BinaryTree.post_order_util(root.left, result_arr)
        BinaryTree.post_order_util(root.right, result_arr)
        result_arr.append(root.data)
