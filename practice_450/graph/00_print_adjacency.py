def create_adjacency_list(n, m, edges: [[]]):
    adjacency_list = {}
    for i in range(m):
        edge = edges[i]
        from_node = edge[0]
        to_node = edge[1]
        if from_node in adjacency_list:
            adjacency_list[from_node].append(to_node)
        else:
            adjacency_list[from_node] = [to_node]

        if to_node in adjacency_list:
            adjacency_list[to_node].append(from_node)
        else:
            adjacency_list[to_node] = [from_node]
    final_list = []

    for i in range(n):
        if i in adjacency_list:
            data = [i]
            data.extend(adjacency_list[i])
        else:
            data = [i]

        final_list.append(data)

    return final_list


if __name__ == '__main__':
    edge_data = [[1, 2]]

    print(create_adjacency_list(3, 1, edge_data))

    edge_data = [[0, 1], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
    print(create_adjacency_list(5, 7, edge_data))
