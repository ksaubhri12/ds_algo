# In top we were taking root as first and then left and right
# In bottom we have to take bottom element first for that vertical level so we will go to left node
# then right node and then root node. This way we will deal with the lead node first


from Node import Node


def bottom_view(root: Node):
    value_dict = {}
    bottom_view_util(root, value_dict, 0)
    copy_dict = value_dict
    keys = list(copy_dict.keys())
    keys.sort()
    sorted_dict = {i: copy_dict[i] for i in keys}
    answer = []
    for value in sorted_dict.values():
        answer.append(value)
    return answer


def bottom_view_util(root: Node, value_dict: {}, level: int):
    if root is None:
        return
    bottom_view_util(root.left, value_dict, level - 1)
    bottom_view_util(root.right, value_dict, level + 1)
    if level not in value_dict:
        value_dict[level] = root.data


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

    print(bottom_view(node_1))

    anode_1 = Node(1)
    anode_2 = Node(3)
    anode_3 = Node(2)
    anode_1.left = anode_2
    anode_1.right = anode_3

    print(bottom_view(anode_1))
