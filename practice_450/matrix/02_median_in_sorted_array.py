def median_in_sorted_arr(matrix: [[]], row: int, col: int):
    median = row * col // 2 + 1
    return kth_smallest(matrix, row, col, median)


def get_element_greater_than_equal_to(num: int, row: int, col: int, mat: [[]]):
    ans = 0
    for i in range(0, row):

        if mat[i][0] > num:
            return ans

        if mat[i][col - 1] < num:
            ans += col
            continue

        greater_than = 0
        jump = col // 2
        while jump >= 1:
            while greater_than + jump < col and mat[i][greater_than + jump] <= num:
                greater_than += jump
            jump //= 2

        ans += greater_than + 1
    return ans


def kth_smallest(matrix: [[]], row: int, col: int, k):
    l, r = matrix[0][0], matrix[row - 1][col - 1]

    while l <= r:
        mid = l + (r - l) // 2
        greater_than_or_equal_to_mid = get_element_greater_than_equal_to(mid, row, col, matrix)

        if greater_than_or_equal_to_mid >= k:
            r = mid - 1
        else:
            l = mid + 1

    return l


if __name__ == '__main__':
    input_matrix = [[1, 3, 5],
                    [2, 6, 9],
                    [3, 6, 9]]
    print(median_in_sorted_arr(input_matrix, 3, 3))
    input_matrix = [[1], [2], [3]]
    print(median_in_sorted_arr(input_matrix, 3, 1))
