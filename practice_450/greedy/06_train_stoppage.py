def max_train_stoppage(trains: [], n, m):
    trains = sorted(trains, key=sort_by_end_time)
    platform_map = {}
    for i in range(0, n):
        platform = trains[i][2]
        if platform in platform_map:
            platform_map[platform].append(trains[i])
        else:
            platform_map[platform] = [trains[i]]

    count = 0
    for platform in platform_map.keys():
        trains = platform_map[platform]
        count = count + max_train_stoppage_platform_util(trains)
    return count


def sort_by_end_time(trains: []):
    return trains[1]


def max_train_stoppage_platform_util(trains: []):
    platform_count = 0
    prev_end = 0
    for train in trains:
        curr_start = train[0]
        if curr_start >= prev_end:
            platform_count = platform_count + 1
            prev_end = train[1]
    return platform_count


if __name__ == '__main__':
    print(
        max_train_stoppage([[950, 1005, 1], [1000, 1030, 1], [1015, 1030, 1], [1200, 1205, 2], [1215, 1230, 2]], 5, 2))
    print(
        max_train_stoppage([[1200, 1210, 1], [1205, 1220, 1], [1215, 1230, 1], [1215, 1240, 1]], 4, 1)
    )

    print(
        max_train_stoppage([[1200, 1210, 1], [1205, 1220, 1], [1215, 1230, 1], [1215, 1240, 1]], 4, 1)
    )

    print(max_train_stoppage([[1000, 1030, 1], [1050, 1100, 1], [1100, 1130, 1]], 3, 1))
