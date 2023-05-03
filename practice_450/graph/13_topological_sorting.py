def topological_sorting(v, adj_graph: [[]]):
    data_stack = []
    visited = [False] * v
    for i in range(v):
        if not visited[i]:
            dfs_util(i, visited, data_stack, adj_graph)
    return list(reversed(data_stack))


def dfs_util(vertex: int, visited: [], data_stack: [], graph: [[]]):
    if visited[vertex]:
        return
    visited[vertex] = True
    for neighbor in graph[vertex]:
        dfs_util(neighbor, visited, data_stack, graph)
    data_stack.append(vertex)


if __name__ == '__main__':
    adj_data = [[], [0], [0], [0]]
    print(topological_sorting(4, adj_data))
