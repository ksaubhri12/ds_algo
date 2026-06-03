def adj_list_from_edges(V, edges):
    adj_graph = []
    for i in range(V):
        adj_graph.append([])

    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]
        adj_graph[from_edge].append(to_edge)
        adj_graph[to_edge].append(from_edge)
    return adj_graph


def dfs_util(visited, low_arr, time_arr, curr_time, node, adj_graph, parent, bridges):
    visited[node] = True
    time_arr[node] = low_arr[node] = curr_time[0]
    curr_time[0] += 1
    for neighbour in adj_graph[node]:
        if neighbour == parent:
            continue
        if not visited[neighbour]:
            dfs_util(visited, low_arr, time_arr, curr_time, neighbour, adj_graph, node, bridges)
            low_arr[node] = min(low_arr[node], low_arr[neighbour])
            if low_arr[neighbour] <= time_arr[node]:
                bridges.append([node, neighbour])
        else:
            low_arr[node] = min(low_arr[node], low_arr[neighbour])


def check_bridge(V, edges, c, d):
    adj_graph = adj_list_from_edges(V, edges)
    visited = [False] * V
    time_arr = [float("inf")] * V
    low_arr = [float("inf")] * V
    timer = [1]
    bridges = []
    for i in range(V):
        if not visited[i]:
            dfs_util(visited, low_arr, time_arr, timer, 0, adj_graph, -1, bridges)

    for bridge in bridges:
        if (bridge[0] == c and bridge[1] == d) or (bridge[0] == d and bridge[1] == c):
            return True

    return False


if __name__ == '__main__':
    # print(check_bridge(4, [[0, 1], [1, 2], [2, 3]], 1, 2))
    # print(check_bridge(5, [[0, 1], [0, 3], [1, 2], [2, 0], [3, 4]], 0, 2))
    print(check_bridge(5, [[1, 2], [2, 0], [1, 0], [3, 4], [3, 0]], 2, 0))
