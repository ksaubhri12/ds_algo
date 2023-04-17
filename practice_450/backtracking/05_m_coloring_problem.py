def m_coloring_problem_helper(graph: [[]], color_arr: [], node: int, color_number: int, vertex: int):
    if node == vertex:
        return True

    for i in range(1, color_number + 1):
        if is_safe(graph, color_arr, node, i):
            color_arr[node] = i
            if m_coloring_problem_helper(graph, color_arr, node + 1, color_number, vertex):
                return True

            color_arr[node] = 0

    return False


def is_safe(graph: [[]], color_arr: [], node, color):
    adjacent_neighbours = graph[node]
    for i in range(0, len(adjacent_neighbours)):
        if adjacent_neighbours[i] != 0 and color_arr[i] == color:
            return False

    return True


def graph_color(graph: [[]], k, v):
    color_arr = [0] * v
    return m_coloring_problem_helper(graph, color_arr, 0, k, v)


if __name__ == '__main__':
    graph_arr = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    print(graph_color(graph_arr, 2, 4))
