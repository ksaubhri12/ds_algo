def min_number_of_jump(arr: [], n):
    starting = 0
    ending = 0
    jump = 0
    while ending < n:
        jump_values = arr[starting]

        if jump_values + starting >= n - 1:
            jump = jump + 1
            break
        if jump_values < 1:
            return -1
        max_element = index_of_max_element(arr, starting + 1, starting + jump_values)
        ending = max_element
        starting = ending
        jump = jump + 1

    return jump


def index_of_max_element(arr: [], start: int, end: int):
    max_element_index = start
    max_element = arr[start]
    for i in range(start, end + 1):
        element = arr[i] + i
        max_element = max(max_element, element)
        if element == max_element:
            max_element_index = i

    return max_element_index


if __name__ == '__main__':
    print(min_number_of_jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11))
    print(min_number_of_jump([1, 4, 3, 2, 6, 7], 6))
    print(min_number_of_jump([0, 1, 1, 1, 1], 5))
    print(min_number_of_jump([9, 10, 1, 2, 3, 4, 8, 0, 0, 0, 0, 0, 0, 0, 1], 15))
