def tug_of_war_helper(input_arr: [], index: int, subset_1: [], subset_2: [], sos_1: int, sos_2: int, result_arr: []):
    if index == len(input_arr):
        delta = abs(sos_1 - sos_2)
        if delta < result_arr[0]:
            result_arr[0] = delta
            result_arr[1] = [subset_1.copy(), subset_2.copy()]
        return

    if len(subset_1) < int((len(input_arr) + 1) / 2):
        subset_1.append(input_arr[index])
        tug_of_war_helper(input_arr, index + 1, subset_1, subset_2, sos_1 + input_arr[index], sos_2, result_arr)
        subset_1.pop(-1)

    if len(subset_2) < int((len(input_arr) + 1) / 2):
        subset_2.append(input_arr[index])
        tug_of_war_helper(input_arr, index + 1, subset_1, subset_2, sos_1, sos_2 + input_arr[index], result_arr)
        subset_2.pop(-1)


def tug_of_war(input_arr: []):
    result_arr = [float('inf'), []]
    tug_of_war_helper(input_arr, 0, [], [], 0, 0, result_arr)
    return result_arr


if __name__ == '__main__':
    print(tug_of_war([3, 4, 5, -3, 100, 1, 89, 54, 23, 20]))
