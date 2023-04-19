def kth_permutation(input_arr: [], n, k, result_arr: [], path_arr: []):
    if n == 0:
        result_arr.append(path_arr.copy())

    for i in range(n):
        element_to_pick = input_arr[i]
        path_arr.append(element_to_pick)
        kth_permutation(input_arr[0:i] + input_arr[i + 1:], n - 1, k, result_arr, path_arr)
        path_arr.pop(-1)


def all_permutation(n, k):
    input_arr = [(i + 1) for i in range(n)]
    result_arr = []
    kth_permutation_v2(input_arr, 0, n, result_arr)
    result_arr = sorted(result_arr)
    element = result_arr[k - 1]
    return [int(i) for i in element]


def kth_permutation_v2(input_arr: [], index: int, n: int, result_arr: []):
    if index == n:
        result_arr.append(''.join([str(i) for i in input_arr]))

    for i in range(index, n):
        input_arr[i], input_arr[index] = input_arr[index], input_arr[i]
        kth_permutation_v2(input_arr, index + 1, n, result_arr)
        input_arr[i], input_arr[index] = input_arr[index], input_arr[i]


if __name__ == '__main__':
    print(all_permutation(3, 6))
    print(all_permutation(2, 2))
