from Node import Node


def construct_binary_tree_from_string(string_value: str):
    if len(string_value) == 1:
        value = int(string_value)
        return Node(value)


