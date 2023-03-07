def sort_col_wise_sorted_matrix(N, Mat):
    final_result = []
    for i in range(0, N):
        for j in range(0, N):
            final_result.append(Mat[i][j])

    final_result = sorted(final_result)
    for i in range(0, N):
        for j in range(0, N):
            Mat[i][j] = final_result.pop(0)

    return Mat



if __name__ == '__main__':
    print(sort_col_wise_sorted_matrix())