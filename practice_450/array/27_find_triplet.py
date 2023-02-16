def find_triplet_with_given_sum(arr: [], n, k):
    arr = sorted(arr)
    for i in range(0, n):
        if i > n - 1:
            break
        element = arr[i]
        start_pointer = i + 1
        end_pointer = n - 1
        sum_value = k - element
        exist_element = two_pointer_for_sum(arr, sum_value, start_pointer, end_pointer)
        if exist_element != -1:
            return True

    return False


def two_pointer_for_sum(arr: [], k, start_pointer, end_pointer):
    while start_pointer < end_pointer:
        curr_sum = arr[start_pointer] + arr[end_pointer]
        if curr_sum == k:
            return start_pointer
        elif curr_sum > k:
            end_pointer = end_pointer - 1
        elif curr_sum < k:
            start_pointer = start_pointer + 1

    return -1


if __name__ == '__main__':
    print(find_triplet_with_given_sum([1, 4, 45, 6, 10, 8], 6, 13))
    print(find_triplet_with_given_sum([1, 2, 4, 3, 6], 5, 10))
    print(find_triplet_with_given_sum([1, 2, 2, 1], 4, 3))
