def value_equal_index(arr: [], n):
    final_result = []
    for i in range(0, n):
        if arr[i] == i + 1:
            final_result.append(i + 1)

    return final_result


if __name__ == '__main__':
    print(value_equal_index([15, 2, 45, 12, 7], 5))
