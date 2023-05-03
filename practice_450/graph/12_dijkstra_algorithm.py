from queue import PriorityQueue


def shortest_distance(v, adj: [[[]]], source_vertex: int):
    data_queue = PriorityQueue()
    visited_dist_map = {}
    for i in range(v):
        visited_dist_map[i] = [False, float('inf')]

    visited_dist_map[source_vertex][1] = 0

    data_queue.put((0, source_vertex))
    while len(data_queue.queue) > 0:
        vertex_weight_data = data_queue.get()
        dist = vertex_weight_data[0]
        vertex = vertex_weight_data[1]
        if visited_dist_map[vertex][0]:
            continue
        visited_dist_map[vertex][0] = True
        for neighbor_weight in adj[vertex]:
            neighbor = neighbor_weight[0]
            weight = neighbor_weight[1]
            curr_dist = visited_dist_map[neighbor][1]
            if curr_dist > weight + dist:
                visited_dist_map[neighbor][1] = weight + dist
                data_queue.put((weight + dist, neighbor))
    final_arr = []
    for value in visited_dist_map.values():
        final_arr.append(value[1])
    return final_arr


if __name__ == '__main__':
    adj_data = [[[1, 9]], [[0, 9]]]
    print(shortest_distance(2, adj_data, 0))

    adj_data = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
    print(shortest_distance(3, adj_data, 2))
