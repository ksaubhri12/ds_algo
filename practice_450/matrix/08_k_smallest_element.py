def get_element_greater_than_equal_to(num: int, n: int, mat: [[]]):
    ans = 0
    for i in range(0, n):

        if mat[i][0] > num:
            return ans

        if mat[i][n - 1] < num:
            ans += n
            continue

        greater_than = 0
        jump = n // 2
        while jump >= 1:
            while greater_than + jump < n and mat[i][greater_than + jump] <= num:
                greater_than += jump
            jump //= 2

        ans += greater_than + 1
    return ans


def kth_smallest(mat: [[]], n, k):
    l, r = mat[0][0], mat[n - 1][n - 1]

    while l <= r:
        mid = l + (r - l) // 2
        greater_than_or_equal_to_mid = get_element_greater_than_equal_to(mid, n, mat)

        if greater_than_or_equal_to_mid >= k:
            r = mid - 1
        else:
            l = mid + 1

    return l


if __name__ == '__main__':
    input_matrix = [
        [9, 12, 20, 25, 35],
        [15, 17, 23, 28, 45],
        [21, 31, 38, 40, 51],
        [28, 41, 47, 52, 62],
        [38, 43, 48, 56, 65]
    ]
    print(kth_smallest(input_matrix, 5, 21))

    input_matrix = [[16, 28, 60, 64],
                    [22, 41, 63, 91],
                    [27, 50, 87, 93],
                    [36, 78, 87, 94]]
    print(kth_smallest(input_matrix, 4, 3))
    input_matrix = [[10, 20, 30, 40],
                    [15, 25, 35, 45],
                    [24, 29, 37, 48],
                    [32, 33, 39, 50]]
    print(kth_smallest(input_matrix, 4, 7))
