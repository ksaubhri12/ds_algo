def two_sum(arr:[], target):
    complimentary_map = {}
    n = len(arr)
    for i in range(n):
        element = arr[i]
        comp_element = target - element
        if comp_element in complimentary_map:
            return [i, complimentary_map[comp_element]]
        else:
            complimentary_map[element] = i


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
