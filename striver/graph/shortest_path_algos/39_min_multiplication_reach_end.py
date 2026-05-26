import heapq


def min_multiplication(start, end, numbers: []):
    heap = [(0, start)]
    dist = [float("inf")] * 1000
    dist[start] = 0

    while heap:

        steps, item_popped = heapq.heappop(heap)
        if steps > dist[item_popped]:
            continue

        for number in numbers:
            new_number = (number * item_popped) % 1000

            if dist[new_number] > steps + 1:
                dist[new_number] = steps + 1
                heapq.heappush(heap, (steps + 1, new_number))

    return dist[end] if dist[end] != float("inf") else -1


if __name__ == '__main__':
    print(min_multiplication(3, 30, [2, 5, 7]))
    print(min_multiplication(7, 175, [3, 4, 65]))
    print(min_multiplication(3, 5, [2, 4]))
