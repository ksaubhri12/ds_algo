from collections import deque


def interleave_queue(input_queue: deque):
    new_queue = deque()
    n = input_queue.__len__()
    for i in range(0, n // 2):
        new_queue.append(input_queue.popleft())

    for i in range(0, n // 2):
        ele_1 = new_queue.popleft()
        ele_2 = input_queue.popleft()
        input_queue.append(ele_1)
        input_queue.append(ele_2)

    return input_queue


if __name__ == '__main__':
    input_data = deque()
    arr_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    [input_data.append(i) for i in arr_list]
    print(interleave_queue(input_data))
