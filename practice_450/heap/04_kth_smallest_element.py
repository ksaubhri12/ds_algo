from queue import PriorityQueue


def k_smallest_element(input_arr: [], n: int, k: int):
    data_queue = PriorityQueue()
    for i in range(k):
        data_queue.put(-input_arr[i])

    for i in range(k, n):
        curr_element = input_arr[i]
        max_element = - 1 * data_queue.get()
        if curr_element < max_element:
            data_queue.put(curr_element * -1)
        else:
            data_queue.put(max_element * -1)

    return data_queue.get() * -1


if __name__ == '__main__':
    print(k_smallest_element([6, 5, 4, 8, 7], 5, 2))
    print(k_smallest_element([1, 3, 2, 6, 5], 5, 4))
    print(k_smallest_element([1, 2, 3, 4, 5], 5, 3))
