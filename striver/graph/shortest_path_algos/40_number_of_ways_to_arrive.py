"""
We have to find number of ways that are minimum in
IN dijkastra, we will keep a way array that will be equivalent to previous one
when you get same short distance then you increment it
"""
import heapq


def adj_list_from_edges(V, edges):
    adj_graph = []
    for i in range(V):
        adj_graph.append([])

    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]
        weight = edge[2]
        adj_graph[from_edge].append([to_edge, weight])
        adj_graph[to_edge].append([from_edge, weight])

    return adj_graph


def total_ways_min(V, edges):
    adj_graph = adj_list_from_edges(V, edges)
    ways = [0] * V
    dist = [float("inf")] * V
    ways[0] = 1
    dist[0] = 0

    heap = [(0, 0)]
    while heap:

        curr_dist, node = heapq.heappop(heap)

        if curr_dist > dist[node]:
            continue

        for neighbour, weight in adj_graph[node]:

            if dist[neighbour] == curr_dist + weight:
                ways[neighbour] += ways[node]

            elif dist[neighbour] > curr_dist + weight:
                dist[neighbour] = curr_dist + weight
                ways[neighbour] = ways[node]
                heapq.heappush(heap, (curr_dist + weight, neighbour))

    return ways[V - 1]


if __name__ == '__main__':
    print(total_ways_min(4, [[0, 1, 2], [1, 2, 3], [0, 3, 5], [1, 3, 3], [2, 3, 4]]))

    print(total_ways_min(6,  [[0, 2, 3], [0, 4, 2], [0, 5, 7], [2, 3, 1], [2, 5, 5], [5, 3, 3], [5, 1, 4], [1, 4, 1], [4, 5, 5]]))
