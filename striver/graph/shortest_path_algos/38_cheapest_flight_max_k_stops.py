import heapq


def adj_graph_from_edges(n, edges):
    adj_graph = []
    for i in range(n):
        adj_graph.append([])

    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]
        weight = edge[2]
        adj_graph[from_edge].append([to_edge, weight])

    return adj_graph


def cheapest_flight_k_stops(n, edges, src, dst, stops):
    adj_graph = adj_graph_from_edges(n, edges)
    dist = [float("inf")] * n

    dist[src] = 0
    heap = [(0, [src, 0])]
    while heap:
        curr_stop, item_popped = heapq.heappop(heap)
        node = item_popped[0]
        curr_dist = item_popped[1]

        if curr_stop > stops:
            continue

        for neighbour, weight in adj_graph[node]:
            if dist[neighbour] > curr_dist + weight:
                dist[neighbour] = curr_dist + weight
                heapq.heappush(heap, (curr_stop + 1, [neighbour, dist[neighbour]]))

    return dist[dst]


if __name__ == '__main__':
    print(cheapest_flight_k_stops(6, [[0, 1, 10], [1, 2, 20], [1, 3, 10], [2, 5, 30], [3, 4, 10], [4, 5, 10]], 0, 5, 2))
    print(cheapest_flight_k_stops(3, [[0, 1, 10], [0, 2, 50], [1, 2, 10]], 0, 2, 1))
