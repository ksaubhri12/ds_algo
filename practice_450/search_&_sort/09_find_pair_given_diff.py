def find_pair_with_given_diff(arr: [], L, N):
    arr = sorted(arr)
    answer = -1
    for i in range(0, L):
        element = arr[i]
        elements_to_search = N + element
        index = binary_search(arr, 0, L - 1, elements_to_search)
        if index != -1:
            answer = 1
            break

    return answer


def binary_search(arr: [], start: int, end: int, k):
    if start >= end and arr[start] == k:
        return start

    if start >= end and arr[start] != k:
        return -1

    middle_index = int((start + end) / 2)

    middle_element = arr[middle_index]

    if middle_element < k:
        return binary_search(arr, middle_index + 1, end, k)
    else:
        return binary_search(arr, start, middle_index, k)


if __name__ == '__main__':
    # print(find_pair_with_given_diff([5, 20, 3, 2, 5, 80], 6, 78))
    # print(find_pair_with_given_diff([90, 70, 20, 80, 50], 5, 45))
    arr = [3327, 6546, 9191, 5756, 3544, 9033, 2221, 6794, 1292, 607, 5685, 160, 5485, 6104, 844, 2842, 6313, 4734,
           5040, 6083, 7795, 9336, 5941, 5322, 9319, 4863, 5905, 4166, 52, 9372, 7282, 9730, 2269, 6473, 5485, 5813,
           1857, 4057, 2606, 9501, 4663, 8290, 9660, 147, 4394, 504, 9340, 706, 1589, 4380, 3141, 5735, 3715, 9081,
           7408, 9385, 3943, 3312, 3550, 346, 9036, 831, 75, 1304, 3655, 1911, 7116, 5512, 2319, 6073, 1364, 3333, 715,
           1023, 9831, 5108, 7878, 9170, 2165, 5819, 3549, 1657, 1553, 3615, 737, 8961, 2999, 1031, 8624, 2900, 7728,
           7659, 83, 4154, 5315, 3737, 6064, 8782, 5600, 4734, 4855, 6963, 8066, 5569, 4338, 7896, 7028, 2215, 7066,
           5544, 8033, 6966, 7201, 5938, 6933, 4289]
    print(find_pair_with_given_diff(arr, 116, 265))
