def min_time_kill_all_snipers(n, m, edges):
    adj_graph = create_adj_list(n, edges)
    get_top_vertex_stack = get_top_sort(adj_graph, n)

    visited_map = {}
    for i in range(n):
        visited_map[i] = [False, float('-inf')]

    while len(get_top_vertex_stack) > 0:
        top_stack_popped = get_top_vertex_stack.pop(-1)
        if visited_map[top_stack_popped][0]:
            continue
        data_queue = [top_stack_popped]
        visited_map[top_stack_popped] = [True, 1]
        while len(data_queue) > 0:

            queue_size = len(data_queue)
            for i in range(queue_size):
                node_pop = data_queue.pop(0)
                time_now = 1 + visited_map[node_pop][1]
                for neighbor in adj_graph[node_pop]:
                    data_queue.append(neighbor)
                    max_time = max(time_now, visited_map[neighbor][1])
                    visited_map[neighbor] = [True, max_time]
    final_arr = [value[1] for value in visited_map.values()]

    return final_arr


def create_adj_list(n, edges) -> [[int]]:
    adj_list = [[] for i in range(n)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])

    return adj_list


def get_top_sort(adj_graph: [[]], v):
    visited = [False] * v
    data_stack = []
    for i in range(v):
        if not visited[i]:
            dfs_util(i, visited, data_stack, adj_graph)
    return data_stack


def dfs_util(vertex: int, visited: [], data_stack: [], adj_graph: [[]]):
    if visited[vertex]:
        return

    visited[vertex] = True
    for neighbor in adj_graph[vertex]:
        dfs_util(neighbor, visited, data_stack, adj_graph)

    data_stack.append(vertex)


if __name__ == '__main__':
    print(min_time_kill_all_snipers(4, 3, [[1, 2], [0, 3], [2, 3]]))
    print(min_time_kill_all_snipers(6, 7, [[1, 2], [1, 0], [0, 2], [0, 4], [5, 4], [5, 3], [3, 4]]))
    print(min_time_kill_all_snipers(4, 5, [[0, 2], [1, 2], [1, 0], [3, 0], [3, 1]]))
    print(min_time_kill_all_snipers(3, 3, [[0, 1], [1, 2], [0, 2]]))
    print(min_time_kill_all_snipers(4, 3, [[1, 2], [0, 3], [2, 3]]))
    print(min_time_kill_all_snipers(3, 2, [[2, 1], [2, 0]]))
