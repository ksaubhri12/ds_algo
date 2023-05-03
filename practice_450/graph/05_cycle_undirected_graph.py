def is_cyclic(graph: [[]], v):
    visited = [False] * v
    for i in range(v):
        if not visited[i]:
            if dfs_util(i, visited, graph, -1):
                return True
    return False


def dfs_util(vertex: int, visited: [], graph: [[]], parent: int):
    visited[vertex] = True

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            if dfs_util(neighbour, visited, graph, vertex):
                return True
        else:
            if neighbour != parent:
                return True


if __name__ == '__main__':
    graph_edge = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
    print(is_cyclic(graph_edge, 5))
    graph_edge = [[], [2], [1, 3], [2]]
    print(is_cyclic(graph_edge, 4))
