def minimize_max_diff_between_heights(arr: [], n, k):
    arr.sort()
    ans = arr[n - 1] - arr[0]
    temp_min = arr[0]
    temp_max = arr[n - 1]

    for i in range(0, n):
        if arr[i] < k:
            continue
        temp_min = min(arr[0] + k - (arr[i] - k), temp_min)