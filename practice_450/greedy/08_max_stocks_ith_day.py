def max_stock_i_th_day(n, k, price: []):
    price_stats = []
    for i in range(0, n):
        price_stats.append([price[i], i + 1])

    price_stats = sorted(price_stats, key=compare_by_price)
    total_spent = 0
    total_stocks = 0
    for i in range(0, n):
        price_stat = price_stats[i]
        price = price_stat[0]
        total_stock_today = price_stat[1]
        if total_spent + total_stock_today * price < k:
            total_spent = total_spent + total_stock_today * price
            total_stocks = total_stocks + total_stock_today
        else:
            money_left_spend = k - total_spent
            stocks_can_buy = money_left_spend // price
            if stocks_can_buy >= 1:
                total_spent = total_spent + stocks_can_buy * price
                total_stocks = total_stocks + stocks_can_buy

    return total_stocks


def compare_by_price(price_stat: []):
    return price_stat[0]


if __name__ == '__main__':
    print(max_stock_i_th_day(3, 45, [10, 7, 19]))
    print(max_stock_i_th_day(3, 100, [7, 10, 4]))
