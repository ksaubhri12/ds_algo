def get_distance_grid(input_grid: [[]]):
    max_row = len(input_grid) - 1
    max_col = len(input_grid[0]) - 1
    input_queue = []
    for i in range(0, max_row + 1):
        for j in range(0, max_col + 1):
            if input_grid[i][j] == 1:
                input_queue.append([i, j])

    output_grid = [[0] * (max_col + 1) for i in range(max_row + 1)]
    for i in range(0, max_row + 1):
        for j in range(0, max_col + 1):
            if input_grid[i][j] == 1:
                output_grid[i][j] = 0
            else:
                output_grid[i][j] = float('inf')

    while len(input_queue) > 0:
        element = input_queue.pop(0)
        curr_row = element[0]
        curr_col = element[1]
        check_and_update_neighbors(curr_row, curr_col, output_grid, input_grid, input_queue, max_row, max_col)

    return output_grid


def check_and_update_neighbors(curr_row: int, curr_col: int, output_grid: [[]], input_grid: [[]], input_queue: [],
                               max_row, max_col):
    move_x = [0, 0, 1, -1]
    move_y = [1, -1, 0, 0]
    for i in range(4):
        new_row = curr_row + move_y[i]
        new_col = curr_col + move_x[i]
        if 0 <= new_row <= max_row and 0 <= new_col <= max_col and output_grid[new_row][new_col] != 0:
            new_dist = output_grid[curr_row][curr_col] + 1
            curr_dist = output_grid[new_row][new_col]
            if new_dist < curr_dist:
                output_grid[new_row][new_col] = new_dist
                input_queue.append([new_row, new_col])


def get_min_dist(curr_row, curr_col, input_data: []):
    min_dist = float('inf')
    for i in range(len(input_data)):
        dist = abs(curr_row - input_data[i][0]) + abs(curr_col - input_data[i][1])
        min_dist = min(min_dist, dist)

    return min_dist


if __name__ == '__main__':
    mat = [[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
    print(get_distance_grid(mat))
