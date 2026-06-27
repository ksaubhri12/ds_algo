from queue import PriorityQueue


def top_k_frequent_element(arr: [], k):
    fre_map = {}
    queue = PriorityQueue()
    for element in arr:
        fre_map[element] = fre_map.get(element, 0) + 1

    i = 0
    keys = list(fre_map.keys())
    for element in keys:
        if i == k:
            break
        freq = fre_map[element]
        fre_map.pop(element)
        queue.put((freq, element))
        i = i + 1

    for element in fre_map.keys():
        freq = fre_map[element]
        peek = queue.queue[0]
        if peek[0] < freq:
            queue.get()
            queue.put((freq, element))

    result = []
    while queue.queue:
        freq, element = queue.get()
        result.append(element)

    return result


if __name__ == '__main__':
    print(top_k_frequent_element([1, 1, 1, 2, 2, 3], 2))
