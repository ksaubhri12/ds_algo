from queue import PriorityQueue
import heapq
from heapq import nsmallest


def get_k_max(input_arr: [], n: int, k: int):
    max_heap = []
    output_arr = []
    for i in range(k):
        heapq.heappush(max_heap, -input_arr[i])

    output_arr.append(-1 * max_heap[0])
    start = 1
    end = k
    while end < n:
        if max_heap[0] == -1 * input_arr[start - 1]:
            heapq.heappop(max_heap)

        heapq.heappush(max_heap, input_arr[end])

        output_arr.append(-max_heap[0])
        start = start + 1
        end = end + 1

    return output_arr


def max_sub_array_size_k(input_arr: [], n: int, k: int):
    data_queue = PriorityQueue()
    if k >= n:
        return [max(input_arr)]

    for i in range(k):
        data_queue.put(-input_arr[i])
    max_element = data_queue.get()
    output_arr = [-1 * max_element]
    data_queue.put(max_element)
    start = 1
    end = k

    while end < n:
        max_element = data_queue.get()
        if -1 * max_element == input_arr[start - 1]:
            data_queue.put(-input_arr[end])
        else:
            data_queue.put(max_element)
            data_queue.put(-input_arr[end])

        answer = data_queue.get()
        output_arr.append(-1 * answer)
        data_queue.put(answer)

        start = start + 1
        end = end + 1

    return output_arr


if __name__ == '__main__':
    print(max_sub_array_size_k([7, 17, 2, 2, 17, 13, 10, 15, 8], 9, 2))
    print(max_sub_array_size_k([10, 7, 8, 11], 4, 2))
    print(max_sub_array_size_k([1, 2, 3, 1, 4, 5, 2, 3, 6], 9, 3))
