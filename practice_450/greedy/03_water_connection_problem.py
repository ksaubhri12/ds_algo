def water_connection_problem(n, p, a, b, d):
    outgoing_map = {}
    ingoing_map = {}
    for i in range(0, p):
        outgoing_map[a[i]] = b[i]

    for i in range(0, p):
        ingoing_map[b[i]] = a[i]

    visited = [-1] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if visited[i] == -1:
            count = count + 1
            process_dfs(visited, i, ingoing_map, outgoing_map)

    return count


def process_dfs(visited: [], house, ingoing_map, outgoing_map):
    if visited[house] != -1:
        return
    visited[house] = 0
    if house in ingoing_map:
        process_dfs(visited, ingoing_map[house], ingoing_map, outgoing_map)
    if house in outgoing_map:
        process_dfs(visited, outgoing_map[house], ingoing_map, outgoing_map)


if __name__ == '__main__':
    print(water_connection_problem(9, 6, [7, 5, 4, 2, 9, 3], [4, 9, 6, 8, 7, 1], [98, 72, 10, 22, 17, 66]))
