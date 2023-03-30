from Node import Node


def check_leaf_node_level(root: Node):
    level_dict = {}
    add_leaf_nodes(root, 0, level_dict)
    if len(level_dict.keys()) > 1:
        return False
    else:
        return True


def add_leaf_nodes(root: Node, level: int, level_dict: {}):
    if root is None:
        return
    add_leaf_nodes(root.left, level + 1, level_dict)
    if root.left is None and root.right is None:
        if level in level_dict:
            level_dict[level].append(root.data)
        else:
            level_dict[level] = [root.data]
    add_leaf_nodes(root.right, level + 1, level_dict)


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(3)
    node_3 = Node(5)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(3)
    node_5 = Node(7)
    node_6 = Node(5)
    node_7 = Node(6)

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    node_8 = Node(6)
    node_4.left = node_8

    print(check_leaf_node_level(node_1))
