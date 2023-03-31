from Node import Node


def max_sum_no_two_adjacent(root: Node):
    if root is None:
        return 0

    root_sum = [float('-inf')]
    max_sum_util(root.right, root_sum)

    return root_sum[0]


def max_sum_util(root: Node, ans: []):
    if root is None:
        return 0

    if root.left is not None:
        ll = max_sum_util(root.left.left, ans)
        lr = max_sum_util(root.left.right, ans)
    else:
        ll = 0
        lr = 0

    if root.right is not None:
        rl = max_sum_util(root.right.left, ans)
        rr = max_sum_util(root.right.right, ans)
    else:
        rl = 0
        rr = 0

    curr_sum_root = root.data + max(ll, lr, rl, rr)
    curr_sum_left = max_sum_util(root.left, ans)
    curr_sum_right = max_sum_util(root.right, ans)
    curr_sum = max(curr_sum_root, curr_sum_right, curr_sum_left)
    if curr_sum > ans[0]:
        print('curr_node_picked_up:{}'.format(root.data))

    ans[0] = max(ans[0], curr_sum)
    return curr_sum


if __name__ == '__main__':
    node_1 = Node(4)
    node_2 = Node(2)
    node_3 = Node(5)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(7)
    node_5 = Node(1)
    node_6 = Node(2)
    node_7 = Node(3)

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    node_8 = Node(6)
    node_5.left = node_8
    print(max_sum_no_two_adjacent(node_1))
