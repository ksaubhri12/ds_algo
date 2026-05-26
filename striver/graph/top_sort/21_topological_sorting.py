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


def topological_sorting(V, edges):
    adj_graph = adj_list_from_edge_data(edges)
    visited = [False] * V
    top_arr = []
    for i in range(V):
        if not visited[i]:
            dfs_util(i, visited, adj_graph, top_arr)

    return top_arr[::-1]


def dfs_util(node, visited, adj_graph, top_arr):
    visited[node] = True
    if node in adj_graph:
        for neighbour in adj_graph[node]:
            if not visited[neighbour]:
                dfs_util(neighbour, visited, adj_graph, top_arr)

    top_arr.append(node)


if __name__ == '__main__':
    print(topological_sorting(4, [[3, 0], [1, 0], [2, 0]]))
    print(topological_sorting(6, [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]))
