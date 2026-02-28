def frog_jump_mem(height_arr, k):
    n = len(height_arr)
    dp_arr = [-1] * n
    dp_arr[0] = 0
    return frog_jump_mem_util(height_arr, k, dp_arr, n - 1)


def frog_jump_mem_util(height_arr, k, dp_arr, index):
    if dp_arr[index] != -1:
        return dp_arr[index]
    min_energy = float("inf")
    for i in range(1, k + 1):
        if index - i >= 0:
            energy = frog_jump_mem_util(height_arr, k, dp_arr, index - i) + abs(
                height_arr[index] - height_arr[index - i])
            min_energy = min(energy, min_energy)
    dp_arr[index] = min_energy
    return dp_arr[index]


def frog_jump_tab(height_arr, k):
    n = len(height_arr)
    dp_arr = [-1] * n
    dp_arr[0] = 0
    for i in range(1, n):
        min_energy = float("inf")
        for j in range(1, k + 1):
            if i - j >= 0:
                jump_energy = dp_arr[i - j] + abs(height_arr[i] - height_arr[i - j])
                min_energy = min(min_energy, jump_energy)
        dp_arr[i] = min_energy
    return dp_arr[n - 1]


if __name__ == '__main__':
    print(frog_jump_tab([10, 30, 40, 20, 50], 2))
    print(frog_jump_mem([10, 30, 40, 20, 50], 2))
    print(frog_jump_tab([30, 10, 60, 10, 60, 50], 2))
