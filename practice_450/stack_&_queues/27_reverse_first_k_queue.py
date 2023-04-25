from queue import Queue


def reverse_k(queue: Queue, k: int):
    data_stack = []
    for i in range(0, k):
        data_stack.append(queue.get())

    while len(data_stack) > 0:
        queue.put(data_stack.pop(-1))

    n = len(queue.queue)
    for i in range(0, n - k):
        x = queue.get()
        queue.put(x)

    return list(queue.queue)


if __name__ == '__main__':
    input_data = Queue()
    input_data.put(4)
    input_data.put(3)
    input_data.put(1)
    input_data.put(10)
    input_data.put(2)
    input_data.put(6)
    print(reverse_k(input_data, 3))
