def max_element_index(center_dist: [], n):
    mi = 0
    for i in range(0, n):
        if center_dist[i] > center_dist[mi]:
            mi = i

    return mi


def k_center_problem(n, k, dist: [[]]):
    center_dist = [float('inf')] * n
    centers = []
    max_center = 0
    for i in range(0, k):
        centers.append(max_center)
        for j in range(0, n):
            center_dist[j] = min(center_dist[j], dist[max_center][j])

        max_center = max_element_index(center_dist, n)

    return center_dist[max_center]


if __name__ == '__main__':
    weights = [[0, 4, 8, 5],
               [4, 0, 10, 7],
               [8, 10, 0, 9],
               [5, 7, 9, 0]]

    print(k_center_problem(4, 2, weights))

    weights = [[0, 10, 7, 6],
               [10, 0, 8, 5],
               [7, 8, 0, 12],
               [6, 5, 12, 0]]

    print(k_center_problem(4, 2, weights))
