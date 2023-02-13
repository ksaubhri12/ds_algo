def count_inversion(arr: [], n):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                # arr[i], arr[j] = arr[j], arr[i]
                count = count + 1
    return count


if __name__ == '__main__':
    print(count_inversion(
        [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462, 492, 496, 443, 328, 437, 392, 105, 403,
         154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370, 413, 168, 300, 36, 395, 204, 312, 323], 42))
