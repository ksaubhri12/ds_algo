# do a pre order traversal
# root, left, right.
# Here take level in horizontal moving and keep them in dict.
# For each level accept only one element which is the first element in that level
# if you go left level will decrease by -1
# if you go right level will increase by +1

from Node import Node


def top_view(root: Node):
    value_dict = {}
    top_view_util(root, value_dict, 0)
    keys = value_dict.keys()
    keys = sorted(keys)
    sorted_dict = {i: value_dict[i] for i in keys}
    return list(sorted_dict.values())


def top_view_util(root: Node, value_dict: {}, level: int):
    if root is None:
        return

    if level not in value_dict:
        value_dict[level] = root.data
    top_view_util(root.left, value_dict, level - 1)

    top_view_util(root.right, value_dict, level + 1)


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

    print(top_view(node_1))


    anode_1 = Node(1)
    anode_2 = Node(2)
    anode_3 = Node(3)
    anode_1.left = anode_2
    anode_1.right = anode_3

    print(top_view(anode_1))
