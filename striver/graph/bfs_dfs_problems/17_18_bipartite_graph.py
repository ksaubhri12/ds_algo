from queue import Queue


def get_color(current_color) -> int:
    if current_color == 0:
        return 1
    else:
        return 0


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


def is_bipartite(vertex, edges) -> bool:
    adj_graph = adj_list_from_edge_data(edges)
    color = [-1] * vertex

    queue = Queue()
    queue.put(0)
    color[0] = 0

    while len(queue.queue) > 0:
        item_popped = queue.get()
        item_color = color[item_popped]

        new_color = get_color(item_color)

        if item_popped in adj_graph:
            for neighbour in adj_graph[item_popped]:
                if color[neighbour] == -1:
                    color[neighbour] = new_color
                    queue.put(neighbour)
                elif color[neighbour] == item_color:
                    return False

    return True


def is_bipartite_dfs(vertex, edges) -> bool:
    adj_graph = adj_list_from_edge_data(edges)
    color_arr = [-1] * vertex
    if not dfs_util(0, color_arr, adj_graph, 0):
        return False

    return True


def dfs_util(node, color_arr, adj_graph, curr_color) -> bool:
    color_arr[node] = curr_color

    new_color = get_color(curr_color)
    if node in adj_graph:
        for neighbour in adj_graph[node]:
            if color_arr[neighbour] == -1:
                if not dfs_util(neighbour, color_arr, adj_graph, new_color):
                    return False
            elif color_arr[neighbour] == curr_color:
                return False

    return True


if __name__ == '__main__':
    print(is_bipartite(3, [[0, 1], [1, 2]]))
    print(is_bipartite(4, [[0, 3], [1, 2], [3, 2], [0, 2]]))
    print(is_bipartite_dfs(3, [[0, 1], [1, 2]]))
    print(is_bipartite_dfs(4, [[0, 3], [1, 2], [3, 2], [0, 2]]))
