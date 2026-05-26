import heapq


def path_with_minimum_effort(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])

    dist = [[float("inf") for _ in range(col_len)] for _ in range(row_len)]
    heap = [(0, [0, 0])]
    dist[0][0] = 0
    neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while heap:
        curr_dist, curr_pos = heapq.heappop(heap)

        curr_row = curr_pos[0]
        curr_col = curr_pos[1]

        if curr_dist > dist[curr_row][curr_col]:
            continue

        for neighbour in neighbours:
            new_row = curr_row + neighbour[0]
            new_col = curr_col + neighbour[1]

            if 0 <= new_row < row_len and 0 <= new_col < col_len:
                curr_diff = abs(matrix[curr_row][curr_col] - matrix[new_row][new_col])
                if dist[new_row][new_col] > max(curr_dist, curr_diff):
                    dist[new_row][new_col] = max(curr_dist, curr_diff)
                    heapq.heappush(heap, (dist[new_row][new_col], [new_row, new_col]))

    return dist[row_len - 1][col_len - 1]


if __name__ == '__main__':
    print(path_with_minimum_effort([[7, 2, 6, 5],
                                    [3, 1, 10, 8]]))
