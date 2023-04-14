# Do three things in recursive manner
# check if left portion is valid and return the height
# check if right portion is valid and return the height
# now check the diff between height is less than or equal to one and also check if the left and right portion is valid
# or not. If the height diff is okay and left and right constraint are also okay then return the height of this node
# and true else false


from Node import Node


def check_balanced_tree(root: Node):
    get_height_bal = check_balanced_tree_util(root)
    return get_height_bal[1]


def check_balanced_tree_util(root: Node):
    if root is None:
        return [0, True]

    left_tree_check_height_bal = check_balanced_tree_util(root.left)
    right_tree_check_height_bal = check_balanced_tree_util(root.right)

    left_tree_check_height = left_tree_check_height_bal[0]
    left_tree_check_bal = left_tree_check_height_bal[1]

    right_tree_check_height = right_tree_check_height_bal[0]
    right_tree_check_bal = right_tree_check_height_bal[1]

    height_diff = abs(left_tree_check_height - right_tree_check_height)

    if height_diff <= 1 and right_tree_check_bal and left_tree_check_bal:
        return [1 + max(left_tree_check_height, right_tree_check_height), True]
    else:
        return [1 + max(left_tree_check_height, right_tree_check_height), False]


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(39)
    node_3 = Node(10)
    node_4 = Node(5)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4

    print(check_balanced_tree(node_1))

    anode_1 = Node(1)
    anode_2 = Node(10)
    anode_3 = Node(5)
    anode_1.left = anode_2
    anode_2.left = anode_3

    print(check_balanced_tree(anode_1))

#     1
#     / \
#             10
#     39
# /
# 5
