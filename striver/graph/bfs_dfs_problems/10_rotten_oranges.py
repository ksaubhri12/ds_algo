"""
If there is a min concepts being used, BFS is the key
to get the min time, we need BFS
"""

from queue import Queue


def rotten_oranges(matrix: [[]]) -> int:
    row_len = len(matrix)
    col_len = len(matrix[0])
    empty_arr = [[0 for _ in range(col_len)] for _ in range(row_len)]
    queue = Queue()

    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == 2:
                queue.put([row, col, 0])

    neighbours_dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    time = 0
    while len(queue.queue) > 0:
        item_pop = queue.get()

        item_row = item_pop[0]
        item_col = item_pop[1]
        item_time = item_pop[2]

        if empty_arr[item_row][item_col] == 2:
            continue

        empty_arr[item_row][item_col] = 2
        time = max(time, item_time)

        for neighbour in neighbours_dir:
            new_row = item_row + neighbour[0]
            new_col = item_col + neighbour[1]
            if is_valid_neighbour(new_row, new_col, row_len, col_len) and matrix[new_row][new_col] == 1:
                queue.put([new_row, new_col, item_time + 1])

    for row in range(row_len):
        for col in range(col_len):
            if empty_arr[row][col] == 0 and matrix[row][col] == 1:
                return -1

    return time


def is_valid_neighbour(row, col, row_len, col_len):
    return 0 <= row < row_len and 0 <= col < col_len


if __name__ == '__main__':
    # print(rotten_oranges([[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]))
    # print(rotten_oranges([[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]]))
    print(rotten_oranges([[0, 1, 2], [0, 1, 2], [2, 1, 1]]))
