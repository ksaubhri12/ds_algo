from Node import Node


class NodeMeta:
    def __init__(self):
        self.is_bst = None
        self.size = None
        self.min = None
        self.max = None


def largest_bst_size(root: Node):
    return largest_bst_binary_tree_util(root).size


def largest_bst_binary_tree_util(root: Node):
    if root is None:
        node_meta = NodeMeta()
        node_meta.is_bst = True
        node_meta.size = 0
        node_meta.min = float('inf')
        node_meta.max = float('-inf')
        return node_meta

    if root.left is None and root.right is None:
        node_meta = NodeMeta()
        node_meta.is_bst = True
        node_meta.size = 1
        node_meta.min = root.data
        node_meta.max = root.data
        return node_meta

    left_side = largest_bst_binary_tree_util(root.left)
    right_side = largest_bst_binary_tree_util(root.right)

    if left_side.is_bst and right_side.is_bst:
        if left_side.max < root.data < right_side.min:
            node_meta = NodeMeta()
            node_meta.is_bst = True
            node_meta.size = left_side.size + right_side.size + 1
            min_value = left_side.min
            max_value = right_side.max
            node_meta.min = root.data if min_value == float('inf') else min_value
            node_meta.max = root.data if max_value == float('-inf') else max_value
            return node_meta

    node_meta = NodeMeta()
    node_meta.is_bst = False
    node_meta.size = max(left_side.size, right_side.size)
    node_meta.min = 0
    node_meta.max = 0

    return node_meta


if __name__ == '__main__':
    node_1 = Node(8)
    node_2 = Node(7)
    node_3 = Node(12)
    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(5)
    node_5 = Node(10)
    node_6 = Node(2)
    node_7 = Node(9)

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    node_8 = Node(2)
    node_9 = Node(6)
    node_10 = Node(10)

    node_4.left = node_8
    node_4.right = node_9

    node_7.right = node_10

    print(largest_bst_size(node_1))
