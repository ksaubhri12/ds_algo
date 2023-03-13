from functools import cmp_to_key


def sort_by_bit(arr: []):
    return sorted(arr, key=cmp_to_key(comparator_function))


def comparator_function(val1, val2):
    bit1 = int(format(val1, 'b'))
    bit2 = int(format(val2, 'b'))
    return bit1 - bit2


if __name__ == '__main__':
    print(sort_by_bit([5, 2, 3, 9, 4, 6, 7, 15, 32]))
