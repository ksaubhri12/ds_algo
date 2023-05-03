def is_cyclic_directed_graph(v, edges: [[]]):
    result_arr = [False]
    visited = [False] * v
    order = [False] * v
    for i in range(v):
        if not visited[i]:
            dfs_util(i, edges, visited, result_arr, order)
        if result_arr[0]:
            return True
    return False


def dfs_util(vertex, graph: [[]], visited: [], result_arr: [], order_vector: []):
    if order_vector[vertex] and visited[vertex]:
        result_arr[0] = True
    if visited[vertex]:
        return

    visited[vertex] = True
    order_vector[vertex] = True
    for neighbour in graph[vertex]:
        dfs_util(neighbour, graph, visited, result_arr, order_vector)

    order_vector[vertex] = False


def get_edge_list(adj_list_data: [[]], v):
    edge_list_data = [[] for i in range(v)]
    for ele in adj_list_data:
        edge_list_data[ele[0]].append(ele[1])

    return edge_list_data


if __name__ == '__main__':
    # edge_list = [[1], [2], [3], [3]]
    # print(is_cyclic_directed_graph(4, edge_list))
    # edge_list = [[1], [2], [3], []]
    # print(is_cyclic_directed_graph(4, edge_list))
    # edge_list = [[4], [10], [1], [2], [5, 6], [6], [8], [0], [9], [3], []]
    # print(is_cyclic_directed_graph(11, edge_list))

    adj_list = [[7, 2], [2, 3], [3, 1], [1, 6], [6, 9], [9, 8], [8, 5], [5, 4], [4, 0], [8, 4], [6, 8], [7, 0], [1, 5],
                [9, 1], [5, 1], [1, 9], [7, 1], [8, 7], [1, 8], [2, 7]]

    edge_list = get_edge_list(adj_list, 10)

    print(is_cyclic_directed_graph(10, edge_list))
