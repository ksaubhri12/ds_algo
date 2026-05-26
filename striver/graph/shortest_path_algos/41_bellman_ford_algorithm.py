def bellman_ford(V, edges, src):
    dist = [float("inf")] * V
    dist[src] = 0

    for i in range(V - 1):
        for edge in edges:
            from_edge = edge[0]
            to_edge = edge[1]
            weight = edge[2]

            if dist[from_edge] + weight < dist[to_edge]:
                dist[to_edge] = dist[from_edge] + weight

    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]
        weight = edge[2]
        if dist[from_edge] + weight < dist[to_edge]:
            return -1

    for i in range(V):
        if dist[i] == float("inf"):
            dist[i] = pow(10, 8)

    return dist


if __name__ == '__main__':
    print(bellman_ford(5, [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]], 0))
    print(bellman_ford(4, [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]], 0))

    print(bellman_ford(7, [[]]))
