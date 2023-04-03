from Node import Node


def predecessor(node: Node):
    pre = node.left
    while pre.right is not None:
        pre = pre.right

    return pre


def successor(node: Node):
    succ = node.right
    while succ.left is not None:
        succ = succ.left

    return succ


def find_succ_prec(root: Node, pre_val: [], succ_val: [], key: int):
    if root is None:
        return
    if root.data == key:
        if root.left is not None:
            pre_val[0] = predecessor(root)
        if root.right is not None:
            succ_val[0] = successor(root)

    if root.data > key:
        succ_val[0] = root
        find_succ_prec(root.left, pre_val, succ_val, key)
    if root.data < key:
        pre_val[0] = root
        find_succ_prec(root.right, pre_val, succ_val, key)


if __name__ == '__main__':
    node_1 = Node(78)
    node_2 = Node(34)
    node_3 = Node(97)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(12)
    node_5 = Node(45)

    node_2.left = node_4
    node_2.right = node_5

    pre_val = [-1]
    succ_val = [-1]

    find_succ_prec(node_1, pre_val, succ_val, 34)
    print(pre_val[0].data, succ_val[0].data)
