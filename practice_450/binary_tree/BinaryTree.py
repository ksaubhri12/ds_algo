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

    @staticmethod
    def in_order_traversal_util(root, result_arr: []):
        if root is None:
            return

        BinaryTree.in_order_traversal_util(root.left, result_arr)
        result_arr.append(root.data)
        BinaryTree.in_order_traversal_util(root.right, result_arr)
