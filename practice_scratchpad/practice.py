class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def build_min_heap(arr: []):
    n = len(arr)
    for i in reversed(range(n // 2)):
        heapify_arr(arr, i, n)
    return arr


def heapify_arr(arr: [], index: int, n):
    smallest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < n and arr[left_index] < arr[smallest]:
        smallest = left_index

    if right_index < n and arr[right_index] < arr[smallest]:
        smallest = right_index

    if smallest != index:
        arr[smallest], arr[index] = arr[index], arr[smallest]
        heapify_arr(arr, smallest, n)


def k_largest_element_array(arr: [], k):
    from queue import PriorityQueue
    n = len(arr)
    pq = PriorityQueue()
    for i in range(k):
        pq.put(arr[i])

    for i in range(k, n):
        curr_element = arr[i]
        bouncer_element = pq.get()
        if curr_element > bouncer_element:
            pq.put(curr_element)
        else:
            pq.put(bouncer_element)

    result_arr = []
    while len(pq.queue):
        result_arr.append(pq.get())

    return list(reversed(result_arr))


def merge_k_sorted_arr(arr: [[]]):
    from queue import PriorityQueue
    pq = PriorityQueue()
    k = len(arr)
    for i in range(k):
        pq.put((arr[i][0], i, 0, len(arr[i])))
    result_arr = []
    while len(pq.queue):
        element_popped, arr_number, index, arr_len = pq.get()
        result_arr.append(element_popped)
        if index == arr_len - 1:
            continue
        pq.put((arr[arr_number][index + 1], arr_number, index + 1, arr_len))

    return result_arr


from queue import PriorityQueue


def signum_function(min_heap_size, max_heap_size):
    if min_heap_size == max_heap_size:
        return 0
    if min_heap_size > max_heap_size:
        return 1

    return -1


def median_stream(arr: []):
    min_heap = PriorityQueue()
    max_heap = PriorityQueue()

    median = -1
    result_arr = []
    for element in arr:
        median = call_median(min_heap, max_heap, element, median)
        result_arr.append(median)

    return result_arr


def get_avg(min_heap, max_heap):
    return (min_heap.queue[0] + -1 * max_heap.queue[0]) / 2


def call_median(min_heap, max_heap, element, curr_median):
    sig_function = signum_function(len(min_heap.queue), len(max_heap.queue))

    if sig_function == 0:
        if element >= curr_median:
            min_heap.put(element)
            return min_heap.queue[0]
        else:
            max_heap.put(-1 * element)
            return -1 * max_heap.queue[0]

    if sig_function == -1:
        if element >= curr_median:
            min_heap.put(element)
            return get_avg(min_heap, max_heap)
        else:
            lower_half_max_element = -1 * max_heap.get()
            min_heap.put(lower_half_max_element)
            max_heap.put(-1 * element)
            return get_avg(min_heap, max_heap)

    else:
        if element >= curr_median:
            upper_half_min_element = min_heap.get()
            max_heap.put(-1 * upper_half_min_element)
            min_heap.put(element)
            return get_avg(min_heap, max_heap)
        else:
            max_heap.put(-1 * element)
            return get_avg(min_heap, max_heap)


def right_side_view(root: Node):
    traverse_queue = [root]

    result_arr = []
    while traverse_queue:
        size = len(traverse_queue)
        result_arr.append(traverse_queue[0].data)
        for i in range(size):
            element_popped = traverse_queue.pop(0)
            if element_popped.right:
                traverse_queue.append(element_popped.right)
            if element_popped.left:
                traverse_queue.append(element_popped.left)

    return result_arr


def level_order_traversal(root: Node):
    traversal_queue = [root]

    result_arr = []
    while traversal_queue:
        size = len(traversal_queue)
        new_res = [r.data for r in traversal_queue]
        result_arr.append(new_res)
        for i in range(size):
            element_popped = traversal_queue.pop(0)
            if element_popped.left:
                traversal_queue.append(element_popped.left)
            if element_popped.right:
                traversal_queue.append(element_popped.right)

    return result_arr


def valid_parenthesis(bracket_string):
    stack = []
    matching_dict = {')': '(', '}': '{', ']': '['}
    for bracket in bracket_string:
        if bracket in '({[':
            stack.append(bracket)
        else:
            if not stack or stack[-1] != matching_dict[bracket]:
                return False
            else:
                stack.pop()

    return len(stack) == 0


def daily_temperature(temperature_arr: []):
    n = len(temperature_arr)
    stack = []
    result_arr = [0] * n

    for i in range(n):

        curr_temp = temperature_arr[i]
        while stack and curr_temp > temperature_arr[stack[-1]]:
            index_popped = stack.pop()
            result_arr[index_popped] = i - index_popped

        stack.append(i)

    return result_arr


def sum_index(arr: [], target_sum: int):
    element_map = {}
    n = len(arr)
    for i in range(n):
        cur_element = arr[i]
        compliment = target_sum - cur_element
        if compliment in element_map:
            return [element_map[compliment], i]
        else:
            element_map[arr[i]] = i


def meeting_rooms2(start, end):
    pq = PriorityQueue()
    n = len(start)

    final_slot_arr = []
    for i in range(n):
        final_slot_arr.append([start[i], end[i]])

    final_slot_arr.sort(key=lambda x: x[0])

    for i in range(n):
        start_time = final_slot_arr[i][0]
        end_time = final_slot_arr[i][1]

        if pq.queue and start_time >= pq.queue[0]:
            pq.get()
            pq.put(end_time)
        else:
            pq.put(end_time)

    return len(pq.queue)


def trapping_max_rain_water(height_arr: []):
    left, right = 0, len(height_arr) - 1

    if height_arr[left] < height_arr[right]:
        smallest = left
    else:
        smallest = right

    max_water = 0
    while left < right:
        water_save = min(height_arr[left], height_arr[right]) * (right - left)
        max_water = max(water_save, max_water)
        if smallest == left:
            left += 1
            smallest = left
        else:
            right -= 1
            smallest = right

    return max_water


def longest_consecutive_1(arr: []):
    left = 0
    zeros = 0
    n = len(arr)
    best = 0

    for right_index in range(n):
        element = arr[right_index]
        if element == 0:
            zeros += 1

        while zeros > 1:
            if arr[left] == 0:
                zeros -= 1
            left = left + 1

        best = max(best, right_index - left)

    return best


if __name__ == '__main__':
    print(longest_consecutive_1([1, 1, 0, 1]))
    print(longest_consecutive_1([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # expect 5
    print(longest_consecutive_1([1, 1, 1]))  # expect 2
    print(longest_consecutive_1([0, 0, 0]))  # expect 0
    print(longest_consecutive_1([1, 0, 1, 1, 0, 1, 1, 1]))  # expect 5

    print(trapping_max_rain_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(meeting_rooms2([1, 10, 7], [4, 15, 10]))

    print(sum_index([2, 7, 11, 15], 18))
    print(sum_index([1, 2, 3, 3, 5, 8, 4], 6))
    print(daily_temperature([73, 74, 75, 71, 69, 72, 76, 73]))
    print(valid_parenthesis("{[]}"))
    node_1 = Node(10)
    node_2 = Node(20)
    node_3 = Node(30)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(40)
    node_5 = Node(60)

    node_2.left = node_4
    node_2.right = node_5

    print(right_side_view(node_1))
    print(level_order_traversal(node_1))

    print(merge_k_sorted_arr([[1, 2, 3, 4], [2, 2, 3, 4], [5, 5, 6, 6], [7, 8, 9, 9]]))
    print(merge_k_sorted_arr([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(k_largest_element_array([12, 5, 787, 1, 23], 2))
    print(build_min_heap([9, 3, 6, 2, 7]))

    print(median_stream([1, 2, 3]))
    print(median_stream([5, 10, 15]))
    print(median_stream([5, 15, 1, 3]))
    print(median_stream([5, 3, 8]))
    print(median_stream([3, 8]))
