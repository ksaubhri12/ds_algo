def trapping_rain_water(arr: [], n):
    left_array = []
    right_array = [0] * n
    max_element = arr[0]
    for i in range(0, n):
        element = arr[i]
        max_element = max(max_element, element)
        left_array.append(max_element)
    max_element = arr[n - 1]
    for i in range(0, n):
        element = arr[n - 1 - i]
        max_element = max(max_element, element)
        right_array[n - 1 - i] = max_element

    water_collected = 0
    for i in range(1, n - 1):
        hill = arr[i]
        left_most_peak = left_array[i]
        right_most_peak = right_array[i]
        min_peak = min(left_most_peak, right_most_peak)
        if left_most_peak > hill and right_most_peak > hill:
            water_collected = water_collected + min_peak - hill

    return water_collected


if __name__ == '__main__':
    print(trapping_rain_water([3, 1, 2, 4, 0, 1, 3, 2], 8))
