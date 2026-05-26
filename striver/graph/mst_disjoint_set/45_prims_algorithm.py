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


def spanning_tree(V, edges):
    adj_graph = adj_list_from_edges(V, edges)
    heap = [(0, 0, -1)]
    mst_arr = []
    sum_value = 0
    visited = [False] * V
    while heap:
        weight, node, parent = heapq.heappop(heap)

        if visited[node]:
            continue
        visited[node] = True
        if parent != -1:
            mst_arr.append([parent, node])

        sum_value += weight
        for neighbour, weight in adj_graph[node]:
            heapq.heappush(heap, (weight, neighbour, node))

    return sum_value


if __name__ == '__main__':
    print(spanning_tree(3, [[0, 1, 5], [1, 2, 3], [0, 2, 1]]))
    print(spanning_tree(2, [[0, 1, 5]]))
