def search_in_step_arr(arr: [], step: int, target: int):
    i = 0
    n = len(arr)
    while i < n:
        element = arr[i]
        if element == target:
            return i

        diff = abs(target - element)
        max_steps = diff // step
        i = i + max(1, max_steps)

    return -1


if __name__ == '__main__':
    print(search_in_step_arr([4, 5, 6, 7, 6], 1, 6))
    print(search_in_step_arr([20, 40, 50, 70, 70, 60], 20, 80))
