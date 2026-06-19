from queue import PriorityQueue


# Pick a priority queue, everything is sorted in itself,
# Put the first element of each array
# Pop the queue, put the popped element into the result
# put the next element of that array into the queue
# Do this till you exhaust the queue

def merge_k_sorted_arr(input_mat: [[]], k: int):
    data_queue = PriorityQueue()
    for i in range(k):
        data_queue.put((input_mat[i][0], i, 0))

    final_result = []
    while len(data_queue.queue) > 0:
        first_element = data_queue.get()
        row_number = first_element[1]
        col_number = first_element[2]
        if col_number + 1 < len(input_mat[row_number]):
            next_element = input_mat[row_number][col_number + 1]
            data_queue.put((next_element, row_number, col_number + 1))
        final_result.append(first_element[0])

    return final_result


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(merge_k_sorted_arr(mat, 3))
    mat = [[1, 2, 3, 4], [2, 2, 3, 4],
           [5, 5, 6, 6], [7, 8, 9, 9]]
    print(merge_k_sorted_arr(mat, 4))
