from queue import Queue


def reverse_queue(input_queue: Queue):
    if len(input_queue.queue) == 0:
        return

    element_dequeue = input_queue.get()
    reverse_queue(input_queue)
    input_queue.put(element_dequeue)


def reverse_queue_main(input_queue: Queue):
    reverse_queue(input_queue)
    return input_queue.queue


if __name__ == '__main__':
    input_data = Queue()
    input_data.put(4)
    input_data.put(3)
    input_data.put(1)
    input_data.put(10)
    input_data.put(2)
    input_data.put(6)
    print(reverse_queue_main(input_data))
