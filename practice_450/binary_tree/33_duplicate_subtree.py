from Node import Node


def print_duplicate_sub_tree(root: Node):
    string_value_map = {}
    result_arr = []
    set_string_map_data(root, string_value_map, result_arr)
    return result_arr


def set_string_map_data(root: Node, string_value_map: {}, result_arr: []):
    if root is None:
        return "$"
    final_string = ''
    if root.left is None and root.right is None:
        return str(root.data)
    final_string = final_string + str(root.data) + '-'
    final_string = final_string + set_string_map_data(root.left, string_value_map, result_arr) + '-'
    final_string = final_string + set_string_map_data(root.right, string_value_map, result_arr) + '-'
    if final_string in string_value_map:
        string_value_map[final_string] = string_value_map[final_string] + 1
    else:
        string_value_map[final_string] = 1

    if string_value_map[final_string] == 2:
        result_arr.append(root)

    return final_string


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(4)
    node_5 = Node(2)
    node_6 = Node(4)
    node_2.left = node_4
    # node_2.right = Node(9)
    node_3.left = node_5
    node_3.right = node_6

    node_7 = Node(4)
    node_5.left = node_7
    # print_duplicate_sub_tree(node_1)

    node_1 = Node(2)
    node_2 = Node(1)
    node_3 = Node(11)
    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(11)
    node_5 = Node(1)

    node_2.left = node_4
    node_3.left = node_5
    print_duplicate_sub_tree(node_1)
