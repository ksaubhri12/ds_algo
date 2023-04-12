from queue import PriorityQueue


def min_trading_cost(wines: [], n: int):
    buyer_wine_stats = []
    seller_wine_stats = []

    for i in range(0, n):
        wine = wines[i]
        if wine < 0:
            seller_wine_stats.append([wine, i])
        if wine > 0:
            buyer_wine_stats.append([wine, i])

    total_buyer = len(buyer_wine_stats)
    total_seller = len(seller_wine_stats)
    buyer_count = 0
    seller_count = 0

    cost = 0
    while buyer_count < total_buyer or seller_count < total_seller:
        wine_buyer = buyer_wine_stats[buyer_count][0]
        wine_buyer_home = buyer_wine_stats[buyer_count][1]
        wine_seller = abs(seller_wine_stats[seller_count][0])
        wine_seller_home = seller_wine_stats[seller_count][1]

        trade_wine = min(wine_buyer, wine_seller)
        dist = abs(wine_seller_home - wine_buyer_home)
        cost = cost + dist * trade_wine

        if wine_buyer < wine_seller:
            buyer_count = buyer_count + 1
            seller_wine_stats[seller_count][0] = abs(wine_seller - trade_wine) * -1

        elif wine_buyer > wine_seller:
            seller_count = seller_count + 1
            buyer_wine_stats[buyer_count][0] = abs(wine_buyer - trade_wine)

        else:
            seller_count = seller_count + 1
            buyer_count = buyer_count + 1

    return cost


if __name__ == '__main__':
    print(min_trading_cost([5, -4, 1, -3, 1], 5))
    print(min_trading_cost([-1000, -1000, -1000, 1000, 1000, 1000], 6))
