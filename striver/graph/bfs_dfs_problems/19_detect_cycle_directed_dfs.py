def adj_list_from_edge_data(edges: [[]]):
    adj_list = {}
    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]

        if from_edge not in adj_list:
            adj_list[from_edge] = [to_edge]
        else:
            adj_list[from_edge].append(to_edge)

    return adj_list


def dfs_util(node, visited, path_visited, adj_graph) -> bool:
    visited[node] = True
    path_visited[node] = True

    if node in adj_graph:
        for neighbour in adj_graph[node]:
            if not visited[neighbour]:
                if dfs_util(neighbour, visited, path_visited, adj_graph):
                    return True
            elif path_visited[neighbour]:
                return True

    path_visited[node] = False
    return False


def dfs_detect_cycle(vertex, edges) -> bool:
    adj_graph = adj_list_from_edge_data(edges)
    visited = [False] * vertex
    path_visited = [False] * vertex
    for i in range(vertex):
        if not visited[i]:
            if dfs_util(i, visited, path_visited, adj_graph):
                return True

    return False


if __name__ == '__main__':
    print(dfs_detect_cycle(4, [[0, 1], [1, 2], [2, 0], [2, 3]]))
    print(dfs_detect_cycle(4, [[0, 1], [0, 2], [1, 2], [2, 3]]))
