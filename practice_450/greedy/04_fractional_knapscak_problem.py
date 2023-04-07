from functools import cmp_to_key


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


def comparator(stats_1: Item, stats_2: Item):
    return (stats_2.value / stats_2.weight) - (stats_1.value / stats_1.weight)


def get_max_weight(max_weight, item_arr: [Item], n):
    item_arr = sorted(item_arr, key=cmp_to_key(comparator))
    weight = 0
    value = 0
    for i in range(0, n):
        new_item = item_arr[i]
        new_weight = new_item.weight
        new_value = new_item.value
        if weight == max_weight:
            break
        if weight + new_weight > max_weight:
            allowed_weight = max_weight - weight
            fractional_value = (new_value / new_weight) * allowed_weight
            value = value + fractional_value
            weight = weight + allowed_weight
        else:
            weight = weight + new_weight
            value = value + new_value

    return float(value)


if __name__ == '__main__':
    print(get_max_weight(50, [Item(120, 30), Item(100, 20), Item(60, 10), ], 3))
    print(get_max_weight(50, [Item(60, 10), Item(100, 20)], 2))
