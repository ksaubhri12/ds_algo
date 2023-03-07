def kth_smallest_element(matrix: [[]], n, k):
    if k == 0:
        return matrix[0][0]

    count = k - 1
    i = 0
    j = 0
    while count > 0:
        element_in_front = matrix[i][j + 1]
        element_in_low = matrix[i + 1][j]

        if element_in_low < element_in_front:
            i = i + 1
            j = j
        else:
            i = i
            j = j + 1
        count = count - 1

    return matrix[i][j]


if __name__ == '__main__':
    input_matrix = [[16, 28, 60, 64],
                    [22, 41, 63, 91],
                    [27, 50, 87, 93],
                    [36, 78, 87, 94]]
    # print(kth_smallest_element(input_matrix, 4, 3))
    input_matrix = [[10, 20, 30, 40],
                    [15, 25, 35, 45],
                    [24, 29, 37, 48],
                    [32, 33, 39, 50]]
    print(kth_smallest_element(input_matrix, 4, 7))
