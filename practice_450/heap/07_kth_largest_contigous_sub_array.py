from queue import PriorityQueue


def kth_largest_contiguous_sub_arr(input_arr: [], n, k: int):
    data_queue = PriorityQueue()
    sum_arr = [input_arr[0]]
    for i in range(1, n):
        sum_arr.append(sum_arr[i - 1] + input_arr[i])

    for i in range(n):
        for j in range(i, n):
            if i == 0:
                sum_value = sum_arr[j]
            else:
                sum_value = sum_arr[j] - sum_arr[i - 1]

            if len(data_queue.queue) < k:
                data_queue.put(sum_value)
            else:
                min_element = data_queue.get()
                if min_element < sum_value:
                    data_queue.put(sum_value)
                else:
                    data_queue.put(min_element)

    return data_queue.get()


if __name__ == '__main__':
    print(kth_largest_contiguous_sub_arr([2, 6, 4, 1], 4, 3))
    print(kth_largest_contiguous_sub_arr([3, 2, 1], 3, 5))
