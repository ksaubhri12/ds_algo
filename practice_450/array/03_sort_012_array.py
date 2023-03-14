# Count number of zero, one and two
# First add all the zero, then one and then two

def sort_012_array(arr: [], n):
    zero_count = 0
    one_count = 0
    two_count = 0

    for i in range(0, n):
        if arr[i] == 0:
            zero_count = zero_count + 1
        if arr[i] == 1:
            one_count = one_count + 1
        if arr[i] == 2:
            two_count = two_count + 1

    for i in range(0, zero_count):
        arr[i] = 0

    for i in range(zero_count, zero_count + one_count):
        arr[i] = 1

    for i in range(one_count + zero_count, one_count + zero_count + two_count):
        arr[i] = 2

    return arr


if __name__ == '__main__':
    print(sort_012_array([1, 2, 0], 3))
    print(sort_012_array([1, 2, 1, 1, 2, 1, 2, 0, 1, 0, 2, 1], 12))
