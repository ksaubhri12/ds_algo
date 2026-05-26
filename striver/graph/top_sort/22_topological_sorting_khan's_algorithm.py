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


def topological_sorting(V, edges):
    adj_graph = adj_list_from_edge_data(edges)
    queue = Queue()

    in_degree_nodes = [0] * V

    for edge in edges:
        to_node = edge[1]
        in_degree_nodes[to_node] += 1

    for node in range(V):
        if in_degree_nodes[node] == 0:
            queue.put(node)
    top_arr = []

    while len(queue.queue) > 0:
        item_popped = queue.get()
        top_arr.append(item_popped)

        if item_popped in adj_graph:
            for neighbour in adj_graph[item_popped]:
                in_degree_nodes[neighbour] -= 1

                if in_degree_nodes[neighbour] == 0:
                    queue.put(neighbour)

    return top_arr


if __name__ == '__main__':
    print(topological_sorting(4, [[3, 0], [1, 0], [2, 0]]))
    print(topological_sorting(6, [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]))
