from queue import PriorityQueue


def min_cost(rope_arr: [], n: int):
    data_queue = PriorityQueue()
    for i in range(n):
        data_queue.put(rope_arr[i])

    cost = 0
    while len(data_queue.queue) > 1:
        first_rope = data_queue.get()
        second_rope = data_queue.get()
        new_rope = first_rope + second_rope
        cost = cost + new_rope
        data_queue.put(new_rope)

    return cost


if __name__ == '__main__':
    print(min_cost([4, 3, 2, 6], 4))
