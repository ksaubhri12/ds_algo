from Node import Node


def height_of_tree(root: Node):
    if root is None:
        return 0

    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)

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

    print(height_of_tree(node_1))
