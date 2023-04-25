# Do In order traversal of the binary tree -> store in arr
# see in how many swaps you can make that arr sorted
# the sorted arr is nothing but in order traversal of BST


from functools import cmp_to_key


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def comparator_function(pair_1: Pair, pair_2: Pair):
    return pair_1.first - pair_2.first


def min_swaps_arr(arr: []):
    pair_list = []
    n = len(arr)
    for i in range(0, n):
        element = arr[i]
        pair = Pair(element, i)
        pair_list.append(pair)
    pair_list = sorted(pair_list, key=cmp_to_key(comparator_function))
    i = 0
    swap = 0
    while i < n:
        if pair_list[i].second == i:
            i = i + 1
            continue
        else:
            index_to_go = pair_list[i].second
            pair_list[i], pair_list[index_to_go] = pair_list[index_to_go], pair_list[i]
            swap = swap + 1

    return swap


if __name__ == '__main__':
    print(min_swaps_arr([10, 50, 60, 40, 30, 20]))
