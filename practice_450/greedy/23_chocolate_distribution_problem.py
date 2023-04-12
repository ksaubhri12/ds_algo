# already solved in array

def chocolate_problem(arr: [], n, m):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(0, n):
        start = i
        end = i + m - 1
        if end < n:
            curr_diff = arr[end] - arr[start]
            min_diff = min(min_diff, curr_diff)

    return min_diff


if __name__ == '__main__':
    print(chocolate_problem([3, 4, 1, 9, 56, 7, 9, 12], 8, 5))
