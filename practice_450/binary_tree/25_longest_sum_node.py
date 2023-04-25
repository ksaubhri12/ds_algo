# We need to compute two things recursively sum of left and right side children
# Also the height of right side and left side children

from Node import Node


def longest_path_driver(root: Node):
    return longest_path(root)[1]


def longest_path(root: Node):
    if root is None:
        return [0, 0]

    if root.left is None and root.right is None:
        return [1, root.data]

    left_tree_height_path = longest_path(root.left)
    right_tree_height_path = longest_path(root.right)
    left_tree_height = left_tree_height_path[0]
    right_tree_height = right_tree_height_path[0]
    left_tree_sum = left_tree_height_path[1]
    right_tree_sum = right_tree_height_path[1]
    if left_tree_height == right_tree_height:
        if left_tree_sum > right_tree_sum:
            return [1 + left_tree_height, root.data + left_tree_sum]
        else:
            return [1 + left_tree_height, root.data + right_tree_sum]

    if left_tree_height > right_tree_height:
        return [1 + left_tree_height, root.data + left_tree_sum]

    else:
        return [1 + right_tree_height, root.data + right_tree_sum]


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.left = node_2
    node_1.right = node_3

    print(longest_path_driver(node_1))

    anode_1 = Node(4)
    anode_2 = Node(2)
    anode_3 = Node(5)
    anode_1.left = anode_2
    anode_1.right = anode_3

    anode_4 = Node(7)
    anode_5 = Node(1)
    anode_6 = Node(2)
    anode_7 = Node(3)
    anode_8 = Node(6)

    anode_2.left = anode_4
    anode_2.right = anode_5
    anode_3.left = anode_6
    anode_3.right = anode_7
    anode_5.left = anode_8

    print(longest_path_driver(anode_1))
