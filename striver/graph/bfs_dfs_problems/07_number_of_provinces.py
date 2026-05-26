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


def number_of_connected_components(vertices, edges: [[]]):
    adj_graph = adj_list_from_edge_data(edges)
    visited = [False] * vertices

    count = 0
    for vertex in range(vertices):
        if not visited[vertex]:
            count = count + 1
            dfs_util(vertex, visited, adj_graph)

    return count


def dfs_util(node, visited: [], graph: dict[int, list[int]]):
    if visited[node]:
        return

    visited[node] = True
    if node in graph:
        for neighbour in graph[node]:
            dfs_util(neighbour, visited, graph)


if __name__ == '__main__':
    print(number_of_connected_components(5, [[0, 1], [2, 1], [3, 4]]))
    print(number_of_connected_components(7, [[0, 1], [6, 0], [2, 4], [2, 3], [3, 4]]))
