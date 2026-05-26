import heapq


def shortest_dist_binary_maze(matrix, src_row, src_col, target_row, target_col):
    row_len = len(matrix)
    col_len = len(matrix[0])
    dist_arr = [[float("inf") for _ in range(col_len)] for _ in range(row_len)]

    heap = [(0, [src_row, src_col])]
    dist_arr[src_row][src_col] = 0
    neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while heap:
        curr_dist, curr_pos = heapq.heappop(heap)

        curr_row = curr_pos[0]
        curr_col = curr_pos[1]

        if curr_dist > dist_arr[curr_row][curr_col]:
            continue

        for neighbour in neighbours:
            new_row = curr_row + neighbour[0]
            new_col = curr_col + neighbour[1]

            if 0 <= new_row < row_len and 0 <= new_col < col_len and matrix[new_row][new_col] == 1:
                if dist_arr[new_row][new_col] > 1 + curr_dist:
                    dist_arr[new_row][new_col] = 1 + curr_dist
                    heapq.heappush(heap, (1 + curr_dist, [new_row, new_col]))

    if dist_arr[target_row][target_col] == float("inf"):
        return -1
    else:
        return dist_arr[target_row][target_col]


if __name__ == '__main__':
    print(shortest_dist_binary_maze(
        [[1, 1, 1, 1],
         [1, 1, 0, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0],
         [1, 0, 0, 1]
         ], 0, 1, 2, 2))

    print(shortest_dist_binary_maze(
        [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0],
         [1, 0, 1, 0, 1]], 0, 0, 3, 4
    ))
