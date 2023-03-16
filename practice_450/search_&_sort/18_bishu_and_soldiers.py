def bishu_soldiers():
    return


# Finding element count lesser than the k
def upper_bound(arr: [], start: int, end: int, k):
    if start > end:
        return start
    middle = start + (end - start) // 2
    middle_element = arr[middle]

    if middle_element == k:
        return upper_bound(arr, start, middle - 1, k)

    if middle_element > k:
        return upper_bound(arr, start, middle - 1, k)

    else:
        return upper_bound(arr, middle + 1, end, k)

# if __name__ == '__main__':
# upper_bound()
