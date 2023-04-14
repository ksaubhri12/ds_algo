def get_max_left_area(width, height, tower_x: [], tower_y: [], n):
    tower_x.append(width + 1)
    tower_y.append(height + 1)

    tower_x = sorted(tower_x)
    tower_y = sorted(tower_y)

    max_width = 0
    prev = 0
    for i in range(0, n):
        width_diff = tower_x[i] - prev - 1
        max_width = max(max_width, width_diff)
        prev = tower_x[i]

    prev = 0
    max_height = 0
    for i in range(0, n):
        height_diff = tower_y[i] - prev - 1
        max_height = max(max_height, height_diff)
        prev = tower_y[i]

    return max_width * max_height


if __name__ == '__main__':
    print(get_max_left_area(15, 8, [3, 11, 8], [8, 2, 6], 3))
