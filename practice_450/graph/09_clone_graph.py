# The idea is to do a DFS
# while doing DFS create a link between parent and current node.
# Store the info and re iterate over that and create new node information.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node):
    curr_head_value = node.val
    visited_dict = {}
    clone_graph_util(node, Node(-1), visited_dict)
    node_creation_dict = {}

    for key in visited_dict:
        key_split = key.split('$')
        from_node = int(key_split[0])
        to_node = int(key_split[1])
        if from_node in node_creation_dict:
            from_node_node = node_creation_dict[from_node]
        else:
            from_node_node = Node(from_node)
            node_creation_dict[from_node] = from_node_node

        if to_node in node_creation_dict:
            to_node_node = node_creation_dict[to_node]
        else:
            to_node_node = Node(to_node)
            node_creation_dict[to_node] = to_node_node

        from_node_node.neighbors.append(to_node_node)
    return node_creation_dict[curr_head_value]


def clone_graph_util(node: Node, parent_node: Node, visited_dict: {}):
    key_1 = get_key(node, parent_node)
    key_2 = get_key(parent_node, node)
    if key_2 in visited_dict or key_1 in visited_dict:
        return

    if parent_node.val != -1:
        key = get_key(node, parent_node)
        visited_dict[key] = 1
        key = get_key(parent_node, node)
        visited_dict[key] = 1

    for neighbor in node.neighbors:
        clone_graph_util(neighbor, node, visited_dict)


def get_key(node: Node, parent_node: Node):
    return str(node.val) + "$" + str(parent_node.val)


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_3, node_1]
    node_3.neighbors = [node_2, node_4]
    node_4.neighbors = [node_1, node_3]

    print(clone_graph(node_1))
