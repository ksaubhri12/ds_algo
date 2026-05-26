from queue import Queue

"""
If I am reaching there and the parent of the node is someone else, then that is the problem
"""


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


def detect_cycle_bfs(vertex, edge_list) -> bool:
    adj_graph = adj_list_from_edge_data(edge_list)
    queue = Queue()
    queue.put([0, -1])
    visited = [False] * vertex

    for start_node in range(vertex):

        if visited[start_node]:
            continue

        queue = Queue()
        queue.put([start_node, -1])
        visited[start_node] = True

        while len(queue.queue) > 0:
            queue_item = queue.get()
            node = queue_item[0]
            parent = queue_item[1]

            if node in adj_graph:
                for neighbour in adj_graph[node]:

                    if not visited[neighbour]:
                        visited[neighbour] = True
                        queue.put([neighbour, node])
                    elif neighbour != parent:
                        return True

    return False


if __name__ == '__main__':
    print(detect_cycle_bfs(4, [[0, 1], [0, 2], [1, 2], [2, 3]]))
    print(detect_cycle_bfs(4, [[0, 1], [1, 2], [2, 3]]))
