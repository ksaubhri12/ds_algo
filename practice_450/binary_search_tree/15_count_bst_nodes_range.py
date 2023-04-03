from Node import Node


def get_count(root: Node, low: int, high: int):
    if root is None:
        return 0

    if low <= root.data <= high:
        return 1 + get_count(root.left, low, high) + get_count(root.right, low, high)

    elif root.data < low:
        return get_count(root.right, low, high)
    else:
        return get_count(root.left, low, high)


if __name__ == '__main__':
    anode_1 = Node(8)
    anode_2 = Node(2)
    anode_3 = Node(18)
    anode_4 = Node(1)
    anode_5 = Node(22)
    anode_1.left = anode_2
    anode_1.right = anode_3

    anode_2.left = anode_4
    anode_3.right = anode_5

    print(get_count(anode_1, 1, 30))
