# def string_count_2d_arr(arr: [[]], input_string: str):
#     row_len = len(arr)
#     col_len = len(arr[0])
#
#     found = 0
#     for i in range(0, row_len):
#         for j in range(0, col_len):
#             found = found + search_string(input_string, 0, arr, i, j, row_len, col_len)
#
#     return found
#
#
# def search_string(input_string, i, arr: [[]], row, col, row_len, col_len):
#     n = len(input_string)
#     if i > n - 1:
#         return 0
#
#
