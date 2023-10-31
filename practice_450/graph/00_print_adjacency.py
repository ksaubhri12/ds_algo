def create_adj_list_v2(n, m, edges):
    adj_list = [[i] for i in range(n)]
    for index in range(len(edges)):
        edge = edges[index]
        from_vertex = edge[0]
        to_vertex = edge[1]
        adj_list[from_vertex].append(to_vertex)
        adj_list[to_vertex].append(from_vertex)

    return adj_list


if __name__ == '__main__':
    edge_data = [[1, 2]]

    print(create_adj_list_v2(3, 1, edge_data))

    edge_data = [[0, 1], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

    print(create_adj_list_v2(5, 7, edge_data))
