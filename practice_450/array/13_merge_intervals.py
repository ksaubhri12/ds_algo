from functools import cmp_to_key


def merge_intervals(arr: [[]]):
    output_arr = []
    arr = sorted(arr, key=cmp_to_key(comparator))

    n = len(arr)
    output_arr.append(arr[0])
    output_arr_last_index = 0
    for i in range(1, n):
        last_merged_range = output_arr[output_arr_last_index]
        curr_range = arr[i]
        start = curr_range[0]
        end = curr_range[1]
        last_merged_range_start = last_merged_range[0]
        last_merged_range_end = last_merged_range[1]
        if start > last_merged_range_end:
            output_arr.append(curr_range)
            output_arr_last_index = output_arr_last_index + 1
        elif last_merged_range_start <= start:
            output_arr[output_arr_last_index] = [last_merged_range_start, max(end, last_merged_range_end)]

    return output_arr


def comparator(arr1: [], arr2: []):
    return arr1[0] - arr2[0]


if __name__ == '__main__':
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge_intervals([[1, 4], [4, 5]]))
    print(merge_intervals([[1, 4], [1, 5]]))
