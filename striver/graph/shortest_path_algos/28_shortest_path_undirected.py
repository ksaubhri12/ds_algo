from queue import Queue


def adj_list_from_edge_data(edges: [[]]):
    adj_list = {}
    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]

        if from_edge not in adj_list:
            adj_list[from_edge] = [to_edge]
        else:
            adj_list[from_edge].append(to_edge)

        if to_edge not in adj_list:
            adj_list[to_edge] = [from_edge]
        else:
            adj_list[to_edge].append(from_edge)

    return adj_list


def shortest_distance(V, edges, src):
    adj_graph = adj_list_from_edge_data(edges)
    dist_arr = [float("inf")] * V
    dist_arr[src] = 0
    queue = Queue()
    queue.put([src, 0])
    while len(queue.queue) > 0:
        item_popped = queue.get()
        node = item_popped[0]
        dist = item_popped[1]

        if node in adj_graph:
            for neighbour in adj_graph[node]:
                if dist_arr[neighbour] > 1 + dist:
                    dist_arr[neighbour] = 1 + dist
                    queue.put([neighbour, dist_arr[neighbour]])

    for i in range(V):
        if dist_arr[i] == float("inf"):
            dist_arr[i] = -1

    return dist_arr


if __name__ == '__main__':
    print(shortest_distance(4, [[0, 3], [1, 3]], 3))
    print(shortest_distance(9,  [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]], 0))
