def max_min_comparison_v2(arr: [], n):
    if n == 1:
        return [arr[0], arr[0]]

    if n == 2:
        first_element = arr[0]
        second_element = arr[1]
        if first_element < second_element:
            return [first_element, second_element]
        else:
            return [second_element, first_element]

    first_half_pair = max_min_comparison_v2(arr[0:n // 2], n // 2)
    second_half_pair = max_min_comparison_v2(arr[n // 2: n], (n - n // 2))

    first_half_max = first_half_pair[1]
    second_half_max = second_half_pair[1]
    overall_max = max(first_half_max, second_half_max)
    overall_min = min(first_half_pair[0], second_half_pair[0])
    return [overall_min, overall_max]


if __name__ == '__main__':
    print(max_min_comparison_v2([3, 5, 4, 1, 9], 5))
    print(max_min_comparison_v2([1000, 11, 445, 1, 330, 3000], 6))
