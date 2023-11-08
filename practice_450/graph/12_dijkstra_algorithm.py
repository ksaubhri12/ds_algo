from queue import PriorityQueue


def shortest_distance(v, adj: [[[]]], source_vertex: int):
    data_queue = PriorityQueue()
    data_queue.put((0, source_vertex))
    visited_map_dict = {}
    for i in range(v):
        visited_map_dict[i] = [False, float('inf')]
    visited_map_dict[source_vertex][1] = 0
    while len(data_queue.queue):
        size = len(data_queue.queue)
        for i in range(size):
            vertex_data = data_queue.get()
            vertex = vertex_data[1]
            dist = vertex_data[0]
            if visited_map_dict[vertex][0]:
                continue
            visited_map_dict[vertex][0] = True
            for neighbour in adj[vertex]:
                neighbour_vertex = neighbour[0]
                weight = neighbour[1]
                curr_dist = visited_map_dict[neighbour_vertex][1]
                if curr_dist > dist + weight:
                    visited_map_dict[neighbour_vertex][1] = dist + weight
                    data_queue.put((dist + weight, neighbour_vertex))

    final_result = []
    for vertex in visited_map_dict:
        dist = visited_map_dict[vertex][1]
        final_result.append(dist)
    return final_result


if __name__ == '__main__':
    adj_data = [[[1, 9]], [[0, 9]]]
    print(shortest_distance(2, adj_data, 0))

    adj_data = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
    print(shortest_distance(3, adj_data, 2))
