def rearrange_positive_negative_number(arr: [], n):
    positive_queue = []
    negative_queue = []
    final_array = []

    for i in range(0, n):
        element = arr[i]
        if element >= 0:
            positive_queue.append(element)
        else:
            negative_queue.append(element)

    i = 0
    while i < n:
        positive_element = None
        negative_element = None
        if len(positive_queue) > 0:
            positive_element = positive_queue.pop(0)
        if len(negative_queue) > 0:
            negative_element = negative_queue.pop(0)
        if positive_element is not None:
            i = i + 1
            final_array.append(positive_element)
        if negative_element is not None:
            i = i + 1
            final_array.append(negative_element)

    return final_array


if __name__ == '__main__':
    print(rearrange_positive_negative_number([9, 4, -2, -1, 5, 0, -5, -3, 2], 9))
