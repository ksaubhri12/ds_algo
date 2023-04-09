def min_pair_sum(arr_1: [], arr_2: [], n: int):
    arr_1 = sorted(arr_1)
    arr_2 = sorted(arr_2)
    result = 0
    for i in range(0, n):
        diff = arr_1[i] - arr_2[i]
        result = result + abs(diff)

    return result


if __name__ == '__main__':
    print(min_pair_sum([4, 1, 8, 7], [2, 3, 6, 5], 4))
    print(min_pair_sum([4, 1, 2], [2, 4, 1], 3))
