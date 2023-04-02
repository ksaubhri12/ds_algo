from Node import Node


def max_sum_no_two_adjacent(root: Node):
    ans = {}
    return max_sum_util(root, ans)


def max_sum_util(root: Node, ans: {}):
    if root is None:
        return 0

    if root in ans:
        return ans[root]

    inc = root.data
    if root.left is not None:
        inc = inc + max_sum_util(root.left.left, ans)
        inc = inc + max_sum_util(root.left.right, ans)
    if root.right is not None:
        inc = inc + max_sum_util(root.right.left, ans)
        inc = inc + max_sum_util(root.right.right, ans)

    exc = max_sum_util(root.left, ans) + max_sum_util(root.right, ans)

    res = max(inc, exc)
    ans[root] = res
    return res



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


    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(1)
    node_5 = Node(4)
    node_6 = Node(5)

    node_2.left = node_4
    node_3.left = node_5
    node_3.right = node_6

    print(max_sum_no_two_adjacent(node_1))
