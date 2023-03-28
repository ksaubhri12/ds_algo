from Node import Node
from BinaryTree import BinaryTree


def sum_tree(root: Node):
    if root is None:
        return root
    sum_tree_util(root)
    return root


def sum_tree_util(root: Node):
    if root is None:
        return [0, True]

    if root.left is None and root.right is None:
        val = root.data
        root.data = 0
        return [val, True]

    if root.left is not None:
        left_node_val = root.left.data
    else:
        left_node_val = 0

    if root.right is not None:
        right_node_val = root.right.data
    else:
        right_node_val = 0
    left_sum_val_terminating = sum_tree_util(root.left)
    right_sum_val_terminating = sum_tree_util(root.right)

    if right_sum_val_terminating[1]:
        final_right_sum = right_sum_val_terminating[0]
    else:
        final_right_sum = right_node_val + right_sum_val_terminating[0]

    if left_sum_val_terminating[1]:
        final_left_sum = left_sum_val_terminating[0]
    else:
        final_left_sum = left_node_val + left_sum_val_terminating[0]

    root.data = final_left_sum + final_right_sum
    return [final_left_sum + final_right_sum, False]


if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(-2)
    node_3 = Node(6)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(8)
    node_5 = Node(-4)

    node_2.left = node_4
    node_2.right = node_5

    node_6 = Node(7)
    node_7 = Node(5)

    node_3.left = node_6
    node_3.right = node_7

    print('Current Binary Tree')
    BinaryTree(node_1).in_order_traversal()
    print('Sum Tree')
    new_node = sum_tree(node_1)
    BinaryTree(new_node).in_order_traversal()



    anode_1 = Node(9)
    anode_2 = Node(6)
    anode_3 = Node(4)
    anode_4 = Node(7)

    anode_1.left = anode_2
    anode_1.right = anode_3
    anode_2.left = anode_4

    print('Current Binary Tree')
    BinaryTree(anode_1).in_order_traversal()
    print('Sum Tree')
    new_node = sum_tree(anode_1)
    BinaryTree(new_node).in_order_traversal()
