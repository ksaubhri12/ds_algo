from queue import Queue


def minimum_distance_matrix(matrix: [[]]) -> [[]]:
    row_len = len(matrix)
    col_len = len(matrix[0])

    dis_matrix = [[0 for _ in range(col_len)] for _ in range(row_len)]

    queue = Queue()
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == 1:
                queue.put([row, col, 0])
                visited[row][col] = True

    neighbours_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while len(queue.queue) > 0:

        item_popped = queue.get()
        item_row = item_popped[0]
        item_col = item_popped[1]
        item_dis = item_popped[2]

        if matrix[item_row][item_col] == 0:
            dis_matrix[item_row][item_col] = item_dis

        for neighbour in neighbours_dir:
            new_row = item_row + neighbour[0]
            new_col = item_col + neighbour[1]

            if 0 <= new_row < row_len and 0 <= new_col < col_len:
                if matrix[new_row][new_col] == 0 and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    queue.put([new_row, new_col, item_dis + 1])

    return dis_matrix


if __name__ == '__main__':
    print(minimum_distance_matrix([[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]))
    print(minimum_distance_matrix([[1, 0, 1], [1, 1, 0], [1, 0, 0]]))
