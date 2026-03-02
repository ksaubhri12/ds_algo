def max_points_rec(points_arr: [[]]):
    days = len(points_arr)
    max_points = float("-inf")
    for activity in [0, 1, 2]:
        points = max_points_rec_util(points_arr, activity, days - 1)
        max_points = max(max_points, points)
    return max_points


def max_points_rec_util(points_arr, activity_index, day_index):
    max_points = float('-inf')
    if day_index == 0:
        return points_arr[0][activity_index]
    if activity_index == 0:
        points = points_arr[day_index][0] + max(max_points_rec_util(points_arr, 1, day_index - 1),
                                                max_points_rec_util(points_arr, 2, day_index - 1))
        max_points = max(max_points, points)
    if activity_index == 1:
        points = points_arr[day_index][1] + max(max_points_rec_util(points_arr, 0, day_index - 1),
                                                max_points_rec_util(points_arr, 2, day_index - 1))
        max_points = max(max_points, points)
    if activity_index == 2:
        points = points_arr[day_index][2] + max(max_points_rec_util(points_arr, 1, day_index - 1),
                                                max_points_rec_util(points_arr, 0, day_index - 1))
        max_points = max(max_points, points)

    return max_points


def max_point_mem(points_arr: [[]]):
    n = len(points_arr)
    dp_arr = [[-1 for _ in range(3)] for _ in range(n)]
    max_points = float("-inf")
    for activity_index in [0, 1, 2]:
        points = max_points_mem_util(points_arr, activity_index, n - 1, dp_arr)
        max_points = max(max_points, points)
    return max_points


def max_points_mem_util(points_arr: [[]], activity_index: int, day_index: int, dp_arr: [[]]):
    if day_index == 0:
        dp_arr[day_index][activity_index] = points_arr[day_index][activity_index]
        return dp_arr[day_index][activity_index]

    if dp_arr[day_index][activity_index] != -1:
        return dp_arr[day_index][activity_index]
    max_points = float('-inf')
    if activity_index == 0:
        points = points_arr[day_index][0] + max(max_points_rec_util(points_arr, 1, day_index - 1),
                                                max_points_rec_util(points_arr, 2, day_index - 1))
        max_points = max(max_points, points)
    if activity_index == 1:
        points = points_arr[day_index][1] + max(max_points_rec_util(points_arr, 0, day_index - 1),
                                                max_points_rec_util(points_arr, 2, day_index - 1))
        max_points = max(max_points, points)
    if activity_index == 2:
        points = points_arr[day_index][2] + max(max_points_rec_util(points_arr, 1, day_index - 1),
                                                max_points_rec_util(points_arr, 0, day_index - 1))
        max_points = max(max_points, points)

    return max_points


def max_points_tab(points_arr: [[]]):
    n = len(points_arr)
    dp_arr = [[-1 for _ in range(3)] for _ in range(n)]
    for i in range(3):
        dp_arr[0][i] = points_arr[0][i]

    for day_index in range(1, n):
        dp_arr[day_index][0] = points_arr[day_index][0] + max(dp_arr[day_index - 1][1], dp_arr[day_index - 1][2])
        dp_arr[day_index][1] = points_arr[day_index][1] + max(dp_arr[day_index - 1][0], dp_arr[day_index - 1][2])
        dp_arr[day_index][2] = points_arr[day_index][2] + max(dp_arr[day_index - 1][0], dp_arr[day_index - 1][1])
    return max(dp_arr[n - 1])


if __name__ == '__main__':
    print(max_points_rec([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
    print(max_points_rec([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
    print(max_points_rec([[4, 2, 6]]))
    print(max_point_mem([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
    print(max_point_mem([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
    print(max_point_mem([[4, 2, 6]]))
    print(max_points_tab([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
    print(max_points_tab([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
    print(max_points_tab([[4, 2, 6]]))
