def adjacency_matrix(nodes, edges, nodes_list: []):
    graph_arr = [[0 for _ in range(edges + 1)] for _ in range(nodes + 1)]
    for nodes in nodes_list:
        first_node = nodes[0]
        second_node = nodes[1]

        graph_arr[first_node][second_node] = 1
        graph_arr[second_node][first_node] = 1


def add_adj_list(adj_list, first_node, second_node):
    if adj_list[first_node] is None:
        adj_list[first_node] = [second_node]
    else:
        adj_list[first_node].append(second_node)


def adjacency_list(nodes, edges, nodes_list: []):
    adj_list = [None] * nodes

    for nodes in nodes_list:
        first_node = nodes[0]
        second_node = nodes[1]
        add_adj_list(adj_list, first_node, second_node)
        add_adj_list(adj_list, second_node, first_node)

    return adj_list


if __name__ == '__main__':
    edge_data = [[0, 1], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
    print(adjacency_list(5, 7, edge_data))
