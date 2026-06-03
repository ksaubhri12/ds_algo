"""
Kosaraju's Algorithm
Sort all the nodes according to the finish time
Reverse the edges
do a DFS again and see what all connected components are
in one go, what all you will be visiting will be strongly connected components
"""


def adj_list_from_edges(V, edges, reverse):
    adj_graph = []
    for i in range(V):
        adj_graph.append([])

    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]
        if reverse:
            adj_graph[to_edge].append(from_edge)
        else:
            adj_graph[from_edge].append(to_edge)

    return adj_graph


def dfs_util(visited, top_arr, node, adj_graph):
    visited[node] = True

    for neighbour in adj_graph[node]:
        if not visited[neighbour]:
            dfs_util(visited, top_arr, neighbour, adj_graph)

    top_arr.append(node)


def find_top_arr(adj_graph, V):
    visited = [False] * V
    top_arr = []

    for i in range(V):
        if not visited[i]:
            dfs_util(visited, top_arr, i, adj_graph)

    return top_arr[::-1]


def strongly_connected_component(V, edges):
    adj_graph = adj_list_from_edges(V, edges, False)
    top_arr = find_top_arr(adj_graph, V)
    new_graph = adj_list_from_edges(V, edges, True)
    visited = [False] * V
    scc_components = []
    for i in range(V):
        element = top_arr[i]
        if not visited[element]:
            new_top_arr = []
            dfs_util(visited, new_top_arr, element, new_graph)
            scc_components.append(new_top_arr)

    return len(scc_components)


if __name__ == '__main__':
    print(strongly_connected_component(5, [[0, 2], [0, 3], [1, 0], [2, 1], [3, 4]]))
    print(strongly_connected_component(3, [[0, 1], [1, 2], [2, 0]]))
