import math


def min_cutter_height(arr: [], n, m):
    start = 0
    end = int(math.pow(2 * 10, 9))
    answer = float('inf')
    height_answer = None
    while start <= end:
        height = start + (end - start) // 2
        wood_cut = 0
        for i in range(0, n):
            element = arr[i]
            wood_cut = wood_cut + max(0, element - height)

        if wood_cut < m:
            end = height - 1
        else:
            if wood_cut < answer:
                answer = wood_cut
                height_answer = height
            start = start + 1

    return height_answer


if __name__ == '__main__':
    print(min_cutter_height([20, 15, 10, 17], 4, 7))
    print(min_cutter_height([4, 42, 40, 26, 46], 5, 20))
