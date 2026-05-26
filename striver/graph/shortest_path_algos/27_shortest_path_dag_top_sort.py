def weight_adj_list_from_edges(edges: [[]]):
    adj_list = {}

    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]
        weight = edge[2]

        if from_edge in adj_list:
            adj_list[from_edge].append([to_edge, weight])
        else:
            adj_list[from_edge] = [[to_edge, weight]]
    return adj_list


def dfs_util(vertex, visited, top_arr, adj_graph):
    visited[vertex] = True

    if vertex in adj_graph:
        for neighbour_weight in adj_graph[vertex]:
            neighbour = neighbour_weight[0]
            if not visited[neighbour]:
                dfs_util(neighbour, visited, top_arr, adj_graph)

    top_arr.append(vertex)


def shortest_path(V, edges, src):
    adj_graph = weight_adj_list_from_edges(edges)
    top_arr = []
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            dfs_util(i, visited, top_arr, adj_graph)

    dist_arr = [float("inf")] * V
    dist_arr[src] = 0

    while top_arr:
        item_popped = top_arr.pop()
        if item_popped in adj_graph:
            for neighbour_weight in adj_graph[item_popped]:
                neighbour = neighbour_weight[0]
                weight = neighbour_weight[1]

                dist_arr[neighbour] = min(dist_arr[neighbour], weight + dist_arr[item_popped])

    for i in range(V):
        if dist_arr[i] == float("inf"):
            dist_arr[i] = -1

    return dist_arr


if __name__ == '__main__':
    print(shortest_path(4, [[0, 1, 2], [0, 2, 1]], 0))
    print(shortest_path(6, [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]], 0))
