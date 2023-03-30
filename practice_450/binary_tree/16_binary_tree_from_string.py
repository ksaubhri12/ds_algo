from Node import Node
from BinaryTree import BinaryTree


def construct_binary_tree_from_string(string_value: str):
    pass


def binary_tree_from_string_helper(si: [], end_index: int, arr: [], root: Node):
    if si[0] >= end_index:
        return None

    if arr[si[0]] == '(':

        if arr[si[0] + 1] != ')':
            if root.left is None:
                if si[0] >= end_index:
                    return
                new_node = Node(arr[si[0] + 1])
                root.left = new_node
                si[0] = si[0] + 2
                binary_tree_from_string_helper(si, end_index, arr, new_node)
        else:
            si[0] = si[0] + 2

        if root.right is None:
            if si[0] >= end_index:
                return

            if arr[si[0]] != '(':
                si[0] = si[0] + 1
                return
            new_node = Node(arr[si[0] + 1])
            root.right = new_node
            si[0] = si[0] + 2
            binary_tree_from_string_helper(si, end_index, arr, root)
        else:
            return

        if arr[si[0]] == ')':
            if si[0] >= end_index:
                return
            si[0] = si[0] + 1
            return
    return


def tree_from_string(string_value: str):
    root = Node(string_value[0])
    if len(string_value) > 1:
        si = [1]
        end_index = len(string_value) - 1
        binary_tree_from_string_helper(si, end_index, string_value, root)

    return root


if __name__ == '__main__':
    new_head_node = tree_from_string('4(2(3)(1))(6(5))')
    tree = BinaryTree(new_head_node)
    tree.in_order_traversal()
    tree.pre_order()
