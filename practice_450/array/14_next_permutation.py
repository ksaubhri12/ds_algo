def next_permutation(arr: []):
    n = len(arr)
    if n == 1:
        return arr
    idx1 = None
    idx2 = None
    for i in reversed(range(0, n - 1)):
        if arr[i] < arr[i + 1]:
            idx1 = i
            break
    if idx1 is None:
        arr[0:n] = reversed(arr[0:n])
        return arr

    min_diff = float('inf')
    for i in reversed(range(idx1 + 1, n)):
        element = arr[i]
        diff = element - arr[idx1]
        if min_diff > diff > 0:
            min_diff = diff
            idx2 = i

    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    arr[idx1 + 1: n] = reversed(arr[idx1 + 1:n])

    return arr


if __name__ == '__main__':
    print(next_permutation([4, 1, 5, 3, 2]))
    print(next_permutation([2, 3, 1]))
