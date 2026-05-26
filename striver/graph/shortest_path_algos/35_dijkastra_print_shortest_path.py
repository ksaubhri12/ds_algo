from queue import Queue
import heapq

def adj_graph_from_edges(V, edges):
    adj = []
    for i in range(V):
        adj.append([])

    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]
        weight = edge[2]
        adj[from_edge].append([to_edge, weight])
        adj[to_edge].append([from_edge, weight])

    return adj


def print_shortest_path(V, edges, src, target):
    adj_graph = adj_graph_from_edges(V, edges)
    dist = [float("inf")] * V

    position_arr = [i for i in range(V)]

    dist[src] = 0
    heap = [(0, src)]

    while heap:

        curr_dist, node = heapq.heappop(heap)

        if curr_dist > dist[node]:
            continue

        for neighbour, weight in adj_graph[node]:

            if dist[neighbour] > curr_dist + weight:
                dist[neighbour] = curr_dist + weight
                heapq.heappush(heap, (dist[neighbour], neighbour))
                position_arr[neighbour] = node

    result_arr = []

    curr = target
    while True:
        previous_node = position_arr[curr]
        if previous_node == curr:
            break
        else:
            result_arr.append(curr)
            curr = previous_node

    return result_arr


if __name__ == '__main__':
    # didn't find the examples in gfg or leet code for this
    print(print_shortest_path(9,
                              [[0, 1, 4], [0, 7, 8], [1, 2, 8], [1, 7, 11], [2, 3, 7], [2, 8, 2], [2, 5, 4], [3, 4, 9],
                               [3, 5, 14], [4, 5, 10], [5, 6, 2], [6, 7, 1], [6, 8, 6], [7, 8, 7]], 0, 8))
