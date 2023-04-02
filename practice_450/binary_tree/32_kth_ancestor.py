from Node import Node


def k_ancestor(root: Node, node_check, k_arr: []):
    if root is None:
        return None

    value_check = root.data == node_check

    if value_check or k_ancestor(root.left, node_check, k_arr) or k_ancestor(root.right, node_check, k_arr):

        if k_arr[0] > 0:
            k_arr[0] = k_arr[0] - 1

        elif k_arr[0] == 0:
            print(root.data)
            return None

        return root


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    k = [2]
    node = 5
    k_ancestor(root, node, k)
