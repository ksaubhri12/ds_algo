def adj_list_from_edge_data(edges: [[]]):
    adj_list = {}
    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]

        if from_edge not in adj_list:
            adj_list[from_edge] = [to_edge]
        else:
            adj_list[from_edge].append(to_edge)

        if to_edge not in adj_list:
            adj_list[to_edge] = [from_edge]
        else:
            adj_list[to_edge].append(from_edge)

    return adj_list


def dfs_util(node, parent_node, visited, adj_graph) -> bool:
    visited[node] = True

    if node in adj_graph:
        for neighbour in adj_graph[node]:
            if not visited[neighbour]:
                if dfs_util(neighbour, node, visited, adj_graph):
                    return True
            elif neighbour != parent_node:
                return True

    return False


def detect_cycle_dfs(vertex, edges) -> bool:
    adj_graph = adj_list_from_edge_data(edges)
    visited = [False] * vertex

    for node in range(vertex):
        if not visited[node]:
            if dfs_util(node, -1, visited, adj_graph):
                return True

    return False


if __name__ == '__main__':
    print(detect_cycle_dfs(4, [[0, 1], [0, 2], [1, 2], [2, 3]]))
    print(detect_cycle_dfs(4, [[0, 1], [1, 2], [2, 3]]))
