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


def dfs_util(node, visited, path_visited, adj_graph, check_node) -> bool:
    visited[node] = True
    path_visited[node] = True

    if node in adj_graph:
        for neighbour in adj_graph[node]:
            if not visited[neighbour]:

                if dfs_util(neighbour, visited, path_visited, adj_graph, check_node):
                    return True
            elif path_visited[neighbour]:
                return True

    path_visited[node] = False
    check_node[node] = 1
    return False


def safest_node(vertex, edges) -> []:
    adj_graph = adj_list_from_edge_data(edges)
    visited = [False] * vertex
    path_visited = [False] * vertex
    check_node = [0] * vertex

    for i in range(vertex):
        if not visited[i]:
            dfs_util(i, visited, path_visited, adj_graph, check_node)

    safe_node = []
    for i in range(vertex):
        if check_node[i] == 1:
            safe_node.append(i)

    return safe_node


if __name__ == '__main__':
    print(safest_node(5, [[1, 0], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]))
    print(safest_node(4, [[1, 2], [2, 3], [3, 2]]))
