# Sort the array first.
# Take the k-1 element since it is a zero based indexing

def kth_min_element(arr: [], n, k):
    arr = sorted(arr)
    return arr[k - 1]


if __name__ == '__main__':
    print(kth_min_element([7, 9, 10, 1, 2], 5, 2))
