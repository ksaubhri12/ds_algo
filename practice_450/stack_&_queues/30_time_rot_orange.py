def time_to_rot_oranges(grid: [[]], max_row, max_col):
    input_data_queue = []
    for i in range(0, max_row + 1):
        for j in range(0, max_col + 1):
            if grid[i][j] == 2:
                input_data_queue.append([i, j])

    input_data_queue.append([-1, -1])
    count = 0
    while len(input_data_queue) > 0:
        element = input_data_queue[0]
        if element[0] == -1 and element[1] == -1 and len(input_data_queue) == 1:
            input_data_queue.pop(0)
            break

        elif element[0] == -1 and element[1] == -1 and len(input_data_queue) > 1:
            input_data_queue.pop(0)
            input_data_queue.append(element)
            count = count + 1
        else:
            rotted_element = input_data_queue.pop(0)
            rotted_row = rotted_element[0]
            rotted_col = rotted_element[1]
            can_be_rotted(rotted_row, rotted_col, max_row, max_col, grid, input_data_queue)

    all_rotten = True
    for i in range(0, max_row + 1):
        for j in range(0, max_col + 1):
            if grid[i][j] == 1:
                all_rotten = False
                break

    return count if all_rotten else -1


def can_be_rotted(rotted_row, rotted_col, max_row, max_col, grid: [[]], input_data_queue: []):
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    for i in range(4):
        new_row = rotted_row + move_y[i]
        new_col = rotted_col + move_x[i]
        if 0 <= new_row <= max_row and 0 <= new_col <= max_col and grid[new_row][new_col] == 1:
            grid[new_row][new_col] = 2
            input_data_queue.append([new_row, new_col])


def get_time(grid: [[]]):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    return time_to_rot_oranges(grid, max_row, max_col)


if __name__ == '__main__':
    mat = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
    print(get_time(mat))
    mat = [[2, 2, 0, 1]]
    print(get_time(mat))
