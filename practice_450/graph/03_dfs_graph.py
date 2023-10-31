def dfs(vertex: int, edges_data: [[]]):
    visited = [False] * (vertex + 1)
    output_arr = []
    dfs_util(visited, 0, edges_data, output_arr)
    return output_arr


def dfs_util(visited: [], vertex: int, edges_data: [[]], output_arr: list):
    if visited[vertex]:
        return
    visited[vertex] = True
    output_arr.append(vertex)
    for neighbour in edges_data[vertex]:
        dfs_util(visited, neighbour, edges_data, output_arr)


if __name__ == '__main__':
    edge_mat = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print(dfs(4, edge_mat))
    edge_mat = [[1, 3], [2, 0], [1], [0]]
    print(dfs(3, edge_mat))
