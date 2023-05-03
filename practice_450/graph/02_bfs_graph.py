from queue import Queue


def graph_bfs(v: int, graph_data: [[]]):
    data_queue = [0]
    output_arr = []
    while len(data_queue) > 0:
        n = len(data_queue)
        for i in range(n):
            element_popped = data_queue.pop(0)
            output_arr.append(element_popped)
            for j in range(v + 1):
                if graph_data[element_popped][j] != 0:
                    data_queue.append(j)

    return output_arr


def graph_bfs_adjacency_list(v: int, graph_data: [[]]):
    adjacency_dict = get_adjacency_dict_from_adjacency_list(graph_data)
    data_queue = Queue()
    data_queue.put(0)
    output_arr = []
    visited = [False] * v
    while len(data_queue.queue) > 0:
        n = len(data_queue.queue)
        for i in range(n):
            element_popped = data_queue.get()
            if visited[element_popped]:
                continue
            visited[element_popped] = True
            output_arr.append(element_popped)
            if element_popped in adjacency_dict:
                neighbours = adjacency_dict[element_popped]
                for neighbour in neighbours:
                    data_queue.put(neighbour)

    return output_arr


def get_adjacency_dict_from_adjacency_list(graph_data: [[]]):
    adjacency_dict = {}
    for element in graph_data:
        from_node = element[0]
        to_node = element[1]
        if from_node in adjacency_dict:
            adjacency_dict[from_node].append(to_node)
        else:
            adjacency_dict[from_node] = [to_node]

    return adjacency_dict


def graph_bfs_edges_min(vertex, edges: [[]]):
    data_queue = Queue()
    data_queue.put(0)
    output_arr = []
    visited = [False] * (vertex + 1)
    while len(data_queue.queue) > 0:
        size = len(data_queue.queue)
        for i in range(size):
            element_popped = data_queue.get()
            if visited[element_popped]:
                continue
            visited[element_popped] = True
            output_arr.append(element_popped)
            neighbours = edges[element_popped]
            for neighbour in neighbours:
                data_queue.put(neighbour)

    return output_arr


if __name__ == '__main__':
    edges_mat = [
        [0, 1],
        [0, 3],
        [1, 2],
        [2, 3]
    ]

    edges_data = [[1, 2, 3], [], [4], [], []]

    print(graph_bfs_edges_min(4, edges_data))
