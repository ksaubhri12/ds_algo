from queue import PriorityQueue


def k_largest_element(input_arr: [], n: int, k: int):
    data_queue = PriorityQueue()
    for i in range(k):
        data_queue.put(input_arr[i])

    for i in range(k, n):
        curr_element = input_arr[i]
        worst_element = data_queue.get()
        if worst_element < curr_element:
            data_queue.put(curr_element)
        else:
            data_queue.put(worst_element)

    final_arr = []
    while len(data_queue.queue) > 0:
        final_arr.append(data_queue.get())

    return list(reversed(final_arr))


if __name__ == '__main__':
    print(k_largest_element([12, 5, 787, 1, 23], 5, 2))
