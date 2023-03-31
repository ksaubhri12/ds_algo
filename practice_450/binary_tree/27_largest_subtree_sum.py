from Node import Node


def larges_sub_tree_sum(root: Node):
    if root is None:
        return 0

    ans = [float('-inf')]
    largest_sub_tree_sum_util(root, ans)
    return ans[0]


def largest_sub_tree_sum_util(root: Node, ans: []):
    if root is None:
        return 0

    curr_sum = root.data + largest_sub_tree_sum_util(root.left, ans) + largest_sub_tree_sum_util(root.right, ans)
    ans[0] = max(ans[0], curr_sum)

    return curr_sum


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(-2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(-6)
    node_7 = Node(2)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    # print(larges_sub_tree_sum(node_1))

    node_1 = Node(-5)
    node_2 = Node(1)
    node_3 = Node(2)
    node_4 = Node(1)
    node_5 = Node(1)
    node_6 = Node(3)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5

    node_3.right = node_6

    print(larges_sub_tree_sum(node_1))
