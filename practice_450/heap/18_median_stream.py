from queue import PriorityQueue


# The idea is to keep 2 heaps for two side of the array, sometime the result will be the peak
# of any of those heap [un even number]
# sometime the result will be the average of these two peak [even number]
# we have to keep these two heaps in such a way that the difference is not more than 1
# for lower half, go with max heap so that you get the max element of the lower half
# for upper half, go with mean heap so that you get the min element of the upper half
# as we have to keep the sorted array

def median_stream(input_arr: []):
    output_arr = []
    min_heap = PriorityQueue()
    max_heap = PriorityQueue()
    median = -1
    n = len(input_arr)
    for i in range(n):
        element = input_arr[i]
        median = call_median(element, min_heap, max_heap, median)
        output_arr.append(median)

    return output_arr


def call_median(element, min_heap: PriorityQueue, max_heap: PriorityQueue, median):
    size_diff = signum_function(len(min_heap.queue), len(max_heap.queue))
    if size_diff == 0:
        if element > median:
            min_heap.put(element)
            return min_heap.queue[0]
        else:
            max_heap.put(element * -1)
            return max_heap.queue[0] * -1

    elif size_diff == 1:
        if element > median:
            max_heap.put(min_heap.get() * -1)
            min_heap.put(element)
            return get_avg_from_both(min_heap, max_heap)

        else:
            max_heap.put(-1 * element)
            return get_avg_from_both(min_heap, max_heap)

    else:
        if element > median:
            min_heap.put(element)
            return get_avg_from_both(min_heap, max_heap)

        else:
            min_heap.put(max_heap.get() * -1)
            max_heap.put(-1 * element)
            return get_avg_from_both(min_heap, max_heap)


def get_avg_from_both(min_heap, max_heap):
    sum_value = min_heap.queue[0] + max_heap.queue[0] * -1
    if sum_value % 2 == 0:
        return sum_value // 2
    else:
        return sum_value // 2


def signum_function(min_heap_size, max_heap_size):
    if min_heap_size == max_heap_size:
        return 0
    elif min_heap_size > max_heap_size:
        return 1
    else:
        return -1


if __name__ == '__main__':
    print(median_stream([1, 2, 3]))
    print(median_stream([5, 10, 15]))
    print(median_stream([5, 15, 1, 3]))
    print(median_stream([5, 3, 8]))
    print(median_stream([3, 8]))
