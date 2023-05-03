from queue import PriorityQueue


def spanning_tree(v, adj: [[[]]]):
    data_queue = PriorityQueue()
    visited = [False] * v
    data_queue.put((0, 0))
    answer = 0
    while len(data_queue.queue) > 0:
        vertex_weight_data = data_queue.get()

        vertex = vertex_weight_data[1]
        if visited[vertex]:
            continue

        visited[vertex] = True
        weight = vertex_weight_data[0]
        answer = answer + weight
        neighbours_weight_list = adj[vertex]
        for neighbour_weight in neighbours_weight_list:
            neighbour = neighbour_weight[0]
            weight = neighbour_weight[1]
            data_queue.put((weight, neighbour))

    return answer


if __name__ == '__main__':
    adj_data = [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]
    print(spanning_tree(3, adj_data))
