from Node import Node
from practice_450.binary_tree.BinaryTree import  BinaryTree


def binary_tree_bst(root: Node):
    inorder_arr = []
    in_order_util(root, inorder_arr)
    sorted_inorder_arr = sorted(inorder_arr)
    elements_map_dict = {}
    for i in range(0, len(inorder_arr)):
        elements_map_dict[inorder_arr[i]] = sorted_inorder_arr[i]

    traverse_queue = [root]
    while len(traverse_queue) > 0:
        size = len(traverse_queue)
        for i in range(0, size):
            element_node = traverse_queue.pop(0)
            curr_value = element_node.data
            desired_value = elements_map_dict[curr_value]
            element_node.data = desired_value
            if element_node.left is not None:
                traverse_queue.append(element_node.left)
            if element_node.right is not None:
                traverse_queue.append(element_node.right)


def in_order_util(root: Node, inorder_arr: []):
    if root is None:
        return
    in_order_util(root.left, inorder_arr)
    inorder_arr.append(root.data)
    in_order_util(root.right, inorder_arr)


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4

    print('Current Binary Tree')
    BinaryTree(node_1).in_order_traversal()
    print('Convert BST')
    binary_tree_bst(node_1)
    BinaryTree(node_1).in_order_traversal()

