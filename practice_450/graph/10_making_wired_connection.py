# Similar to different island problem, we do DFS and the number of times we have to do DFS is
# the number of different clusters we have. If we have two clusters we need 1 wire.
def dfs_util(vertex: int, adj: [[]], visited: []):
    if visited[vertex]:
        return

    visited[vertex] = True
    for neighbor in adj[vertex]:
        dfs_util(neighbor, adj, visited)


def make_wired_connection(n: int, wires: [[]]):
    adj_list = [[] for i in range(n)]
    for wire in wires:
        adj_list[wire[0]].append(wire[1])
        adj_list[wire[1]].append(wire[0])

    total_edges = len(wires)
    min_edges = n - 1
    if min_edges > total_edges:
        return -1

    count = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            count = count + 1
            dfs_util(i, adj_list, visited)

    return count - 1


if __name__ == '__main__':
    wires_list = [[1, 2], [1, 3], [2, 3]]
    print(make_wired_connection(4, wires_list))
    wires_list = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    print(make_wired_connection(6, wires_list))
    wires_list = [[0, 1], [0, 2], [0, 3], [1, 2]]
    print(make_wired_connection(6, wires_list))
