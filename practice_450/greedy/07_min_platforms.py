def min_platforms(n, arr, dep):
    arr = sorted(arr)
    dep = sorted(dep)
    platform_count = 1
    i = 1
    j = 0
    while i < n:
        if arr[i] <= dep[j]:
            platform_count = platform_count + 1
        else:
            j = j + 1
        i = i + 1
    return platform_count


if __name__ == '__main__':
    print(min_platforms(6, [900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))
    print(min_platforms(3, [900, 1100, 1235], [1000, 1200, 1240]))
