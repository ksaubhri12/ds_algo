# The diameter of tree is basically sum of left and right sub tree + 1. It basically like from one end of tree to
# another end traversing length so you will traverse in left equal to left tree height and in right right tree height
# For root it can be different and for any other node it can be different so we have to take max -> that will be
# the diameter of the tree

from Node import Node


def diameter_of_tree(root: Node):
    result_arr = [0]
    diameter_of_tree_util(root, result_arr)
    return result_arr[0]


def diameter_of_tree_util(root: Node, result_arr: []):
    if root is None:
        return 0

    left_height = diameter_of_tree_util(root.left, result_arr)
    right_height = diameter_of_tree_util(root.right, result_arr)

    curr_node_dia = left_height + right_height + 1
    result_arr[0] = max(result_arr[0], curr_node_dia)
    return 1 + max(left_height, right_height)


if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(20)
    node_3 = Node(30)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(40)
    node_5 = Node(60)

    node_2.left = node_4
    node_2.right = node_5

    print(diameter_of_tree(node_1))
