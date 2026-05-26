import heapq


def adj_weight_graph_from_edges(weighted_edges):
    adj_graph = {}

    for weighted_edge in weighted_edges:
        from_edge = weighted_edge[0]
        to_edge = weighted_edge[1]
        weight = weighted_edge[2]

        if not from_edge in adj_graph:
            adj_graph[from_edge] = [[to_edge, weight]]
        else:
            adj_graph[from_edge].append([to_edge, weight])

        if not to_edge in adj_graph:
            adj_graph[to_edge] = [[from_edge, weight]]
        else:
            adj_graph[to_edge].append([from_edge, weight])

    return adj_graph


def dijkstra_algo(V, weighted_edges, src):
    dist = [float("inf")] * V
    dist[src] = 0
    adj_graph = adj_weight_graph_from_edges(weighted_edges)
    heap = [(0, src)]

    while heap:
        curr_dist, node = heapq.heappop(heap)

        if curr_dist > dist[node]:
            continue

        if node in adj_graph:
            for neighbour, weight in adj_graph[node]:
                if dist[neighbour] > curr_dist + weight:
                    dist[neighbour] = curr_dist + weight
                    heapq.heappush(heap, (dist[neighbour], neighbour))

    return dist


if __name__ == '__main__':
    print(dijkstra_algo(3, [[0, 1, 1], [1, 2, 3], [0, 2, 6]], 2))
    print(dijkstra_algo(5, [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]], 0))

