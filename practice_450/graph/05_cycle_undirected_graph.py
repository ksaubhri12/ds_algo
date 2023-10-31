# Video Link -> https://youtu.be/UPfUFoWjk5w?si=MGbfHEVOcoTF1q6_

def dfs_util(vertex: int, visited: [], edges: [[]], parent: int):
    visited[vertex] = True
    for neighbour in edges[vertex]:
        if not visited[neighbour]:
            if dfs_util(neighbour, visited, edges, vertex):
                return True
        else:
            if neighbour != parent:
                return True


def is_cyclic(edges: [[]], vertex):
    visited = [False] * vertex
    for i in range(vertex):
        if not visited[i]:
            if dfs_util(i, visited, edges, None):
                return True

    return False


if __name__ == '__main__':
    graph_edge = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
    print(is_cyclic(graph_edge, 5))
    graph_edge = [[], [2], [1, 3], [2]]
    print(is_cyclic(graph_edge, 4))
