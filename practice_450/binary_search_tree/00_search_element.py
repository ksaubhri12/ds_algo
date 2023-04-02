from practice_450.binary_tree.Node import Node


def search_element(root: Node, element):
    if root is None:
        return False

    if root.data == element:
        return True

    if root.data > element:
        return search_element(root.left, element)
    else:
        return search_element(root.right, element)


if __name__ == '__main__':
    node_1 = Node(2)
    node_2 = Node(81)

    node_1.right = node_2

    node_3 = Node(42)
    node_4 = Node(87)
    node_2.left = node_3
    node_2.right = node_4

    node_5 = Node(66)
    node_6 = Node(90)

    node_3.right = node_5
    node_4.right = node_6

    node_7 = Node(45)
    node_5.left = node_7

    print(search_element(node_1, 87))
