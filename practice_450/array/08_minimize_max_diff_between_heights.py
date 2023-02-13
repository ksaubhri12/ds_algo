from functools import cmp_to_key


class TowerData:
    def __init__(self):
        self.value = None
        self.index = None


def comparator(tower1: TowerData, tower2: TowerData):
    return tower1.value - tower2.value


def minimize_max_diff_between_heights(arr: [], n, k):
    arr = sorted(arr)
    min_height = arr[0]
    max_height = arr[n - 1]
    ans = max_height - min_height
    for i in range(1, n):
        if arr[i] < k:
            continue
        temp_max_height = max(arr[i - 1] + k, arr[n - 1] - k)
        temp_min_height = min(arr[0] + k, arr[i] - k)
        ans = min(ans, temp_max_height - temp_min_height)

    return ans


if __name__ == '__main__':
    print(minimize_max_diff_between_heights([7, 4, 8, 8, 8, 9], 6, 6))
