def first_negative_number(input_arr: [], n, k):
    output_arr = []
    input_data_queue = []
    for i in range(n):
        if input_arr[i] < 0:
            input_data_queue.append(i)

    if len(input_data_queue) == 0:
        return [0] * (n - k + 1)

    start = 0
    end = k - 1
    while end < n:
        if len(input_data_queue) == 0:
            output_arr.append(0)
            start = start + 1
            end = end + 1
            continue
        curr_negative_index = input_data_queue[0]
        if start <= curr_negative_index <= end:
            output_arr.append(input_arr[curr_negative_index])
        else:
            output_arr.append(0)

        if start == curr_negative_index:
            input_data_queue.pop(0)

        start = start + 1
        end = end + 1

    return output_arr


if __name__ == '__main__':
    print(first_negative_number([-8, 2, 3, -6, 10], 5, 2))
    print(first_negative_number([12, -1, -7, 8, -15, 30, 16, 28], 8, 3))
