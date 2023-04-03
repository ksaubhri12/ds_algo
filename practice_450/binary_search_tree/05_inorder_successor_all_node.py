class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class BinaryTreeUtil:
    def __init__(self, root: Node):
        self.root = root

    def print_tree(self):
        curr = self.root
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next
        print()


def inorder_successor_all_nodes(root: Node):
    result_arr = []
    inorder_successor_util(root, result_arr)
    for i in range(0, len(result_arr) - 1):
        result_arr[i].next = result_arr[i + 1]
    return root


def inorder_successor_util(root: Node, result_arr: []):
    if root is None:
        return
    inorder_successor_util(root.left, result_arr)
    result_arr.append(root)
    inorder_successor_util(root.right, result_arr)

if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(8)
    node_3 = Node(12)

    node_4 = Node(3)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4

    print('Populate inorder traversal')
    inorder_successor_all_nodes(node_1)
    BinaryTreeUtil(node_1).print_tree()
