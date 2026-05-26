"""
Using BFS here
"""

from queue import Queue


def adj_list_from_edge_data(edges: [[]]):
    # opposite graph we need outdegree 0, equivalent to top sorting of indegree 0
    adj_list = {}
    for edge in edges:
        from_edge = edge[0]
        to_edge = edge[1]

        if to_edge not in adj_list:
            adj_list[to_edge] = [from_edge]
        else:
            adj_list[to_edge].append(from_edge)

    return adj_list


def safe_node(V, edges) -> []:
    adj_graph = adj_list_from_edge_data(edges)

    in_degree_node = [0] * V

    for edge in edges:
        from_node = edge[0]
        in_degree_node[from_node] += 1

    queue = Queue()
    for i in range(V):
        if in_degree_node[i] == 0:
            queue.put(i)
    safe_node = []
    while len(queue.queue) > 0:
        item_popped = queue.get()

        safe_node.append(item_popped)

        if item_popped in adj_graph:
            for neighbour in adj_graph[item_popped]:

                in_degree_node[neighbour] -= 1

                if in_degree_node[neighbour] == 0:
                    queue.put(neighbour)

    return safe_node


if __name__ == '__main__':
    print(safe_node(5, [[1, 0], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]))
    print(safe_node(4, [[1, 2], [2, 3], [3, 2]]))