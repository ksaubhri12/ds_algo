def shop_candy_store(candies: [], n, k):
    candies = sorted(candies)
    min_item = get_item_sorted_candy(candies, n, k)
    candies = list(reversed(candies))
    max_item = get_item_sorted_candy(candies, n, k)
    return [min_item, max_item]


def get_item_sorted_candy(candies: [], n: int, k):
    i = 0
    j = n - 1
    price_paid = 0
    while i <= j:
        price_paid = price_paid + candies[i]
        i = i + 1
        j = j - k

    return price_paid


if __name__ == '__main__':
    print(shop_candy_store([3, 2, 1, 4], 4, 2))
    print(shop_candy_store([3, 2, 1, 4, 5], 5, 4))
    print(shop_candy_store([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 0))
    print(shop_candy_store([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 1))
    print(shop_candy_store([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 2))
