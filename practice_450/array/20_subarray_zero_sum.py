def sub_array_zero_sum(arr: []):
    n = len(arr)
    prefix_sum_dict = {}
    sum_value = 0

    for i in range(0, n):
        sum_value = sum_value + arr[i]
        if arr[i] == 0:
            return True
        elif sum_value in prefix_sum_dict:
            return True
        elif sum_value == 0:
            return True
        else:
            prefix_sum_dict[sum_value] = 1

    return False


if __name__ == '__main__':
    print(sub_array_zero_sum([4, 2, -3, 1, 6]))
    print(sub_array_zero_sum([4, 2, 0, 1, 6]))
