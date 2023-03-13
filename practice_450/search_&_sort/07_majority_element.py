def majority_element(arr: [], n):
    majority_element_value = arr[0]
    count = 1
    for i in range(1, n):
        element = arr[i]
        if element == majority_element_value:
            count = count + 1

        if element != majority_element_value:
            count = count - 1

        if count == 0:
            majority_element_value = element
            count = 1

    final_count = 0
    if count < 1:
        return -1

    for i in range(0, n):
        if arr[i] == majority_element_value:
            final_count = final_count + 1

    if final_count > n / 2:
        return majority_element_value
    else:
        return -1


if __name__ == '__main__':
    print(majority_element([1, 3, 3, 4, 3], 5))
    print(majority_element([1, 2, 3], 3))
    print(majority_element([3, 1, 3, 3, 2], 5))
