from Node import Node


def count_pairs(root_1: Node, root_2: Node, sum_value):
    dict_map_1 = {}
    in_order_util(root_1, dict_map_1)
    dict_map_2 = {}
    in_order_util(root_2, dict_map_2)
    count = 0
    for key in dict_map_1:
        need = sum_value - key
        if need in dict_map_2:
            
            count = count + 1

    return count


def in_order_util(root: Node, dict_map: {}):
    if root is None:
        return
    in_order_util(root.left, dict_map)
    dict_map[root.data] = 1
    in_order_util(root.right, dict_map)


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(3)
    node_3 = Node(2)

    node_1.right = node_2
    node_2.left = node_3

    anode_1 = Node(3)
    anode_2 = Node(2)
    anode_3 = Node(4)
    anode_1.left = anode_2
    anode_1.right = anode_3
    anode_4 = Node(1)
    anode_2.left = anode_4

    print(count_pairs(node_1, anode_1, 4))
