from Node import Node


def is_isomorphic(root_1: Node, root_2: Node):
    if root_1 is None and root_2 is None:
        return True

    if root_1 is None or root_2 is None:
        return False

    if root_1.data != root_2.data:
        return False

    one_condition = is_isomorphic(root_1.left, root_2.left) and is_isomorphic(root_1.right, root_2.right)
    swap_condition = is_isomorphic(root_1.left, root_2.right) and is_isomorphic(root_1.right, root_2.left)

    return one_condition or swap_condition


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4

    cnode_1 = Node(1)
    cnode_2 = Node(3)
    cnode_3 = Node(2)
    cnode_4 = Node(4)
    cnode_1.left = cnode_2
    cnode_1.right = cnode_3
    cnode_2.left = cnode_4

    # print(is_isomorphic(node_1, cnode_1))

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4

    cnode_1 = Node(1)
    cnode_2 = Node(3)
    cnode_3 = Node(2)
    cnode_4 = Node(4)
    cnode_1.left = cnode_2
    cnode_1.right = cnode_3
    cnode_3.right = cnode_4

    print(is_isomorphic(node_1, cnode_1))
