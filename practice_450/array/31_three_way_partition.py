def three_way_partition(arr: [], a, b):
    n = len(arr)
    low_bucket_count = 0
    middle_bucket_count = 0
    upper_bucket_count = 0
    for i in range(0, n):
        element = arr[i]
        if element < a:
            low_bucket_count = low_bucket_count + 1
        elif a <= element < b:
            middle_bucket_count = middle_bucket_count + 1
        else:
            upper_bucket_count = upper_bucket_count + 1

    temp = 0
    element = arr[temp]
    low_starting_index = 0
    middle_starting_index = low_starting_index + low_bucket_count
    upper_starting_index = middle_starting_index + middle_bucket_count
    while low_bucket_count + middle_bucket_count + upper_bucket_count > 0:
        if element < a:
            to_pick_index = low_starting_index
            if temp == to_pick_index:
                temp = temp + 1
                element = arr[to_pick_index]
            else:
                temp = to_pick_index
                arr[to_pick_index], element = element, arr[to_pick_index]
            low_starting_index = low_starting_index + 1
            low_bucket_count = low_bucket_count - 1
        elif a <= element < b:
            to_pick_index = middle_starting_index
            if temp == to_pick_index:
                temp = temp + 1
                element = arr[to_pick_index]
            else:
                temp = to_pick_index
                arr[to_pick_index], element = element, arr[to_pick_index]
            middle_starting_index = middle_starting_index + 1
            middle_bucket_count = middle_bucket_count - 1
        else:
            to_pick_index = upper_starting_index
            if temp == to_pick_index:
                temp = temp + 1
                element = arr[to_pick_index]
            else:
                temp = to_pick_index
                arr[to_pick_index], element = element, arr[to_pick_index]
            upper_starting_index = upper_starting_index + 1
            upper_bucket_count = upper_bucket_count - 1
    return arr


if __name__ == '__main__':
    # print(three_way_partition([1, 2, 3, 3, 4], 1, 2))
    # print(three_way_partition([1, 2, 3], 1, 3))
    print(three_way_partition([87, 78, 16, 94], 36, 72))
