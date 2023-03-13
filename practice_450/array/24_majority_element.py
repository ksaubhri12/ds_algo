# This we did using sorting and window of k.
# This is not exactly majority element Moore's Voting

def majority_element(arr: []):
    n = len(arr)
    k = int(n / 3)
    arr = sorted(arr)
    left = 0
    result_arr = {}
    right = k + left
    while right < n:
        element_at_left = arr[left]
        element_at_right = arr[right]
        if element_at_left == element_at_right:
            result_arr[element_at_left] = 1
        left = left + 1
        right = k + left

    return list(result_arr.keys())


if __name__ == '__main__':
    print(majority_element([3, 2, 3]))
    print(majority_element([1, 2]))
    print(majority_element([2, 2]))
