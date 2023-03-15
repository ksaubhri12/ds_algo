def island_count(arr: [[]], n: int, m: int):
    visited_arr = [0] * (n * m)
    count = 0
    for i in range(0, n):
        for j in range(0, m):
            element = arr[i][j]
            if element == 0:
                continue
            elif is_visited(arr, i, j):
                continue
            else:
                count = count + 1
                do_dfs_mark_visited(arr, i, j, visited_arr)

    return count


def do_dfs_mark_visited(arr: [[]], i, j, visited: []):
    if arr[i][j] == 0:
        return




def is_visited(visited_arr: [], i, j):
    return visited_arr[i + j] == 1
