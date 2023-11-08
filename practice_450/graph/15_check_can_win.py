# Topological Sort is possible in DAG.
# if a graph is cyclic topological sort is not possible

def check_can_kill_all_snipers(n, m, edges):
    adj_graph = create_adj_list(n, edges)
    return False if is_cyclic(adj_graph, n) else True


def create_adj_list(n, edges) -> [[int]]:
    adj_list = [[] for i in range(n)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])

    return adj_list


def is_cyclic(ad_graph: [[]], v):
    visited = [False] * v
    ordered_arr = [False] * v
    result_arr = [False]
    for i in range(v):
        if not visited[i]:
            dfs_util(ad_graph, i, visited, ordered_arr, result_arr)
        if result_arr[0]:
            return True

    return result_arr[0]


def dfs_util(adj_graph: [[]], vertex: [], visited: [], ordered_arr: [], result_arr: []):
    if visited[vertex] and ordered_arr[vertex]:
        result_arr[0] = True

    if visited[vertex]:
        return
    visited[vertex] = True
    ordered_arr[vertex] = True
    for neighbor in adj_graph[vertex]:
        dfs_util(adj_graph, neighbor, visited, ordered_arr, result_arr)

    ordered_arr[vertex] = False
