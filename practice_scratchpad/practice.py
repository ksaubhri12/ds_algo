class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


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


# find unique triplet for which the sum is zero
def three_sum(arr: []):
    arr = sorted(arr)

    n = len(arr)
    result = []
    # n-2 because after i, the next two element will be l and r
    for i in range(n - 2):

        if i > 0 and arr[i] == arr[i - 1]:
            # we have already done this computation before
            continue

        l = i + 1
        r = n - 1

        while l < r:
            total = arr[i] + arr[l] + arr[r]

            if total == 0:
                result.append([arr[i], arr[l], arr[r]])
                while l < r and arr[l] == arr[l + 1]:
                    l = l + 1

                while l < r and arr[r] == arr[r - 1]:
                    r = r - 1
                l += 1
                r -= 1

            elif total > 0:
                r = r - 1  # if total is bigger, it means we need smaller sum so we move the big number which is right

            else:
                l = l + 1  # if total is smaller, it means we need bigger
                # sum so we move the smaller number which is left
    return result


def max_path_sum_util(root: Node, result: []):
    if root is None:
        return 0

    temp = root.data
    left_sum = max_path_sum_util(root.left, result)
    right_sum = max_path_sum_util(root.right, result)
    if left_sum > 0:
        temp += left_sum
    if right_sum > 0:
        temp += right_sum

    result[0] = max(result[0], temp)
    return root.data + max(left_sum, right_sum, 0)


def max_path_sum(root: Node):
    result = [float("-inf")]
    max_path_sum_util(root, result)
    return result[0]


def reverse_linked_list(head: LinkedListNode):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# at any point, the number is either part of the sub array or we start fresh
def max_sub_array(arr: []):
    n = len(arr)
    curr = arr[0]
    best = arr[0]

    for i in range(1, n):
        new_element = arr[i]
        new_addition = new_element + curr
        curr = max(new_element, new_addition)
        best = max(best, curr)

    return best


# prefix product array and suffix product array

def product_of_array(arr: []):
    n = len(arr)

    output = [1] * n

    left = 1
    for i in range(n):
        output[i] = left
        left = left * arr[i]

    right = 1
    for i in range(n - 1, -1, -1):
        output[i] = output[i] * right
        right = right * arr[i]

    return output


def best_time_buy_sell_stock(arr: []):
    n = len(arr)
    max_profit = float("-inf")
    min_price = arr[0]

    for i in range(1, n):
        today_price = arr[i]
        min_price = min(today_price, min_price)
        max_profit = max(max_profit, arr[i] - min_price)
    return max_profit


def length_of_longest_substring(string: str):
    n = len(string)
    l = 0
    r = 0
    best = 0
    char_set = set()
    while r < n:
        if string[r] in char_set:
            char_set.remove(string[l])
            l = l + 1
        else:
            char_set.add(string[r])
            best = max(best, r - l + 1)
            r = r + 1

    return best


def valid_anagram(string_1, string_2):
    dict = {}
    for char in string_1:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    for char in string_2:
        if char in dict:
            dict[char] -= 1
        else:
            return False

    for key in dict.keys():
        if dict[key] != 0:
            return False

    return True


def permutation_check(string_1, string_2):
    if len(string_2) < len(string_1):
        return False
    freq_map_1 = {}
    freq_map_2 = {}
    for i in range(len(string_1)):
        char_1 = string_1[i]
        char_2 = string_2[i]
        if char_2 in freq_map_2:
            freq_map_2[char_2] += 1
        else:
            freq_map_2[char_2] = 1

        if char_1 in freq_map_1:
            freq_map_1[char_1] += 1
        else:
            freq_map_1[char_1] = 1

    window_size = len(string_1)

    l = 0
    r = window_size - 1
    n = len(string_2)
    while r < n:
        if freq_map_1 == freq_map_2:
            return True
        else:
            # remove l
            char_to_remove = string_2[l]
            freq_map_2[char_to_remove] -= 1
            if freq_map_2[char_to_remove] == 0:
                del freq_map_2[char_to_remove]
            l = l + 1
            r = r + 1
            if r < n:
                char_to_add = string_2[r]
                if char_to_add in freq_map_2:
                    freq_map_2[char_to_add] += 1
                else:
                    freq_map_2[char_to_add] = 1

    return False


def character_replacement(input_string: str, k: int):
    max_freq = 0
    freq = {}
    best = 0
    l = 0
    n = len(input_string)

    for r in range(n):
        freq[input_string[r]] = freq.get(input_string[r], 0) + 1
        max_freq = max(max_freq, freq[input_string[r]])

        # This is invalid zone, we just want to get out of here and that is why we are shrinking
        # Nothing best can come out of this zone and that is why no point of tracking max here
        # that is why keeping a single counter of max_freq works
        while (r - l + 1) - max_freq > k:
            freq[input_string[l]] = freq[input_string[l]] - 1
            l = l + 1

        best = max(best, r - l + 1)

    return best


def max_number_of_vowels_in_substring(input_string: str, k):
    count = 0
    best = 0
    n = len(input_string)
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for i in range(k):
        if input_string[i] in vowel_list:
            count = count + 1
            best = max(best, count)

    l = 0
    for i in range(k, n):
        element_to_add = input_string[i]
        element_to_remove = input_string[l]
        if element_to_add in vowel_list:
            count = count + 1
        if element_to_remove in vowel_list:
            count = count - 1
        best = max(best, count)
        l = l + 1

    return best


def kth_smallest_element_bst(root: Node, k, count: []):
    if root is None:
        return None

    left_result = kth_smallest_element_bst(root.left, k, count)
    if left_result is not None:
        return left_result
    count[0] += 1
    if count[0] == k:
        return root.data
    return kth_smallest_element_bst(root.right, k, count)


def count_good_node_util(root: Node, count: [], best_on_path):
    if root is None:
        return None

    if root.data >= best_on_path:
        count[0] += 1
        best_on_path = root.data

    count_good_node_util(root.left, count, best_on_path)
    count_good_node_util(root.right, count, best_on_path)


def count_good_node(root: Node):
    count = [0]
    count_good_node_util(root, count, root.data)
    return count[0]


def add_two_linked_list(node_1: LinkedListNode, node_2: LinkedListNode):
    ## incorrect code
    curr_sum = node_1.data + node_2.data

    if curr_sum >= 10:
        head = LinkedListNode(1)
        head.next = LinkedListNode(10 - curr_sum)
        prev = head.next
    else:
        head = LinkedListNode(curr_sum)
        prev = head

    curr_1 = node_1.next
    curr_2 = node_2.next
    while curr_1 and curr_2:
        curr_sum = curr_1.data + curr_2.data
        if curr_sum >= 10:
            new_node = LinkedListNode(10 - curr_sum)
            prev.data = prev.data + 1
            prev.next = new_node
            prev = new_node

        else:
            new_node = LinkedListNode(curr_sum)
            prev.next = new_node
            prev = new_node

        curr_1 = curr_1.next
        curr_2 = curr_2.next
    return head


if __name__ == '__main__':
    print(max_number_of_vowels_in_substring("abciiidef", 3))
    print(max_number_of_vowels_in_substring("aeiou", 2))
    print(max_number_of_vowels_in_substring("leetcode", 3))
    print(permutation_check("ab", "eidbaooo"))
    print(valid_anagram("anagram", "nagaram"))
    print(valid_anagram("rat", "car"))
    print(length_of_longest_substring("pwwkew"))
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
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
