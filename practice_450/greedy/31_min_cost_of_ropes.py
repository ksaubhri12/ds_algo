from queue import PriorityQueue


def min_cost_rope(rope_arr: []):
    n = len(rope_arr)
    priority_queue = PriorityQueue()
    for i in range(0, n):
        priority_queue.put(rope_arr[i])

    cost = 0
    while len(priority_queue.queue) > 1:
        first_element = priority_queue.get()
        second_element = priority_queue.get()
        new_rope = first_element + second_element
        cost = cost + new_rope
        priority_queue.put(new_rope)

    return cost


if __name__ == '__main__':
    print(min_cost_rope([4, 2, 7, 6, 9]))
    print(min_cost_rope([4, 3, 2, 6]))

