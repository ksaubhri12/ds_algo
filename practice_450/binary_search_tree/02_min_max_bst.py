from Node import Node


def min_element(root: Node):
    if root is None:
        return -1
    if root.left is None:
        return root.data

    curr = root.left
    while curr.left is not None:
        curr = curr.left

    return curr.data


def max_element(root: Node):
    if root is None:
        return -1
    if root.right is None:
        return root
    curr = root.right
    while curr.right is not None:
        curr = curr.right

    return curr.data


if __name__ == '__main__':
    node_1 = Node(9)
    node_2 = Node(10)
    node_3 = Node(11)

    node_1.right = node_2
    node_2.right = node_3

    print(min_element(node_1))
    print(max_element(node_1))

    node_1 = Node(5)
    node_2 = Node(3)
    node_3 = Node(6)
    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(2)
    node_5 = Node(4)
    node_6 = Node(7)
    node_2.left = node_4
    node_2.right = node_5

    node_3.right = node_6

    node_8 = Node(1)
    node_4.left = node_8
    print(min_element(node_1))
    print(max_element(node_1))
