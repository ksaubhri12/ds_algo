from queue import PriorityQueue


def smallest_range(input_arr: [[]], n, k):
    min_ele = float('inf')
    max_ele = float('-inf')
    data_queue = PriorityQueue()
    for i in range(k):
        ele = input_arr[i][0]
        min_ele = min(min_ele, ele)
        max_ele = max(max_ele, ele)
        data_queue.put((ele, i, 0))

    answer_start = min_ele
    answer_end = max_ele
    result = answer_end - answer_start
    while len(data_queue.queue) > 0:
        min_element_popped = data_queue.get()
        min_ele = min_element_popped[0]
        curr_range = max_ele - min_ele
        if curr_range < result:
            answer_end = max_ele
            answer_start = min_ele
            result = curr_range

        if min_element_popped[2] < n - 1:
            row = min_element_popped[1]
            col = min_element_popped[2] + 1
            next_element = input_arr[row][col]
            max_ele = max(max_ele, next_element)
            data_queue.put((next_element, row, col))
        else:
            break

    return [answer_start, answer_end]


if __name__ == '__main__':
    mat = [[1, 3, 5, 7, 9],
           [0, 2, 4, 6, 8],
           [2, 3, 5, 7, 11]]
    print(smallest_range(mat, 5, 3))
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]

    print(smallest_range(mat, 4, 3))