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

    return adj_list


def detect_cycle(V, edges):
    adj_graph = adj_list_from_edge_data(edges)
    in_degree_arr = [0] * V
    queue = Queue()
    for edge in edges:
        to_edge = edge[1]
        in_degree_arr[to_edge] += 1

    for i in range(V):
        if in_degree_arr[i] == 0:
            queue.put(i)

    processed = 0
    while len(queue.queue) > 0:

        item_popped = queue.get()
        processed += 1

        if item_popped in adj_graph:
            for neighbour in adj_graph[item_popped]:

                in_degree_arr[neighbour] -= 1

                if in_degree_arr[neighbour] == 0:
                    queue.put(neighbour)

    return processed != V


if __name__ == '__main__':
    print()
