def path_more_than_k(n, m, k, edges):
    graph_map = {}
    for i in range(0, m):
        edge = edges[i]
        from_node = edge[0]
        to_node = edge[1]
        weightage = edge[2]
        if from_node in graph_map:
            graph_map[from_node].append([to_node, weightage])
        else:
            graph_map[from_node] = [[to_node, weightage]]
    result_arr = [False]
    visited = [0] * n
    visited[0] = 1
    path_traverse_helper(graph_map, visited, 0, 0, k, result_arr)
    ans = result_arr[0]
    return 'YES' if result_arr[0] else 'NO'


def path_traverse_helper(graph_map: {}, visited: [], index, curr_value, k, result_arr: []):
    if curr_value >= k:
        result_arr[0] = True
        return

    if index not in graph_map:
        return
    edges = graph_map[index]
    for edge in edges:
        from_edge = edge[0]
        weightage = edge[1]
        if visited[from_edge] == 0:
            visited[from_edge] = 1
            path_traverse_helper(graph_map, visited, from_edge, curr_value + weightage, k, result_arr)
            visited[from_edge] = 0

    return


if __name__ == '__main__':
    edge_arr = [[0, 1, 5],
                [1, 2, 9],
                [2, 0, 8],
                ]
    print(path_more_than_k(3, 3, 18, edge_arr))

    edge_arr = [[0, 1, 10],
                [0, 2, 13]]
    print(path_more_than_k(3, 2, 10, edge_arr))
