# This needs revision, we need to break [0,4] as [0,1][1,4] + [0,2][2,4] + [0,3][3,4]
# first find the one which have only 1 matrix combo then 2 matrix combo then 3 matrix combo

def matrix_multiplication(n, arr):
    dp_arr = [[0] * n for i in range(n)]
    for length in range(2, n):
        col = length
        for row in range(0, n - length):
            dp_arr[row][col] = float('inf')
            for k in range(row + 1, col):
                new_ans = dp_arr[row][k] + dp_arr[k][col] + arr[row] * arr[k] * arr[col]
                dp_arr[row][col] = min(dp_arr[row][col], new_ans)
            col = col + 1

    return dp_arr[0][n - 1]


if __name__ == '__main__':
    print(matrix_multiplication(5, [2, 3, 4, 1, 3]))
