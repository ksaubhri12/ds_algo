from Node import Node


def check_duplicate(root: Node):
    value_dict = {}
    check_duplicate_util(root, value_dict)
    answer = 0
    for key in value_dict:
        if value_dict[key] > 1:
            answer = 1
            break

    return answer


def check_duplicate_util(root: Node, value_dict: {}):
    if root is None:
        return "$"
    final_string = ''
    if root.left is None and root.right is None:
        return str(root.data)
    final_string = final_string + str(root.data)
    final_string = final_string + check_duplicate_util(root.left, value_dict)
    final_string = final_string + check_duplicate_util(root.right, value_dict)
    if final_string in value_dict:
        value_dict[final_string] = value_dict[final_string] + 1
    else:
        value_dict[final_string] = 1

    return final_string


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(4)
    node_5 = Node(5)

    node_2.left = node_4
    node_2.right = node_5

    node_6 = Node(2)
    node_3.left = node_6

    node_7 = Node(4)
    node_8 = Node(5)

    node_6.left = node_7
    node_6.right = node_8

    print(check_duplicate(node_1))

    node_1 = Node(2)
    node_2 = Node(2)
    node_3 = Node(2)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(3)
    node_2.left = node_4

    node_5 = Node(3)
    node_3.left = node_5

    # print(check_duplicate(node_1))

    node_1 = Node(2)
    node_2 = Node
