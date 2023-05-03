def dfs_graph(v, adj: [[]]):
    visited = [False] * (v + 1)
    output_arr = []
    dfs_utils(0, visited, adj, output_arr)
    return output_arr


def dfs_utils(vertex: int, visited_arr: [], graph: [[]], output_arr: []):
    if visited_arr[vertex]:
        return

    visited_arr[vertex] = True
    output_arr.append(vertex)
    for neighbour in graph[vertex]:
        dfs_utils(neighbour, visited_arr, graph, output_arr)


if __name__ == '__main__':
    edge_mat = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print(dfs_graph(4, edge_mat))
    edge_mat = [[1, 3], [2, 0], [1], [0]]
    print(dfs_graph(3, edge_mat))
