def min_coins(amount, coins, ret_map):
    if amount == 0:
        return ""
    for coin in coins:
        if amount - coin >= 0:
            sub_ans = f"{coin}_" + str(min_coins(amount - coin, coins, ret_map))
            ret_map[sub_ans] = 1
    return ""




def min_coins_util(amount, coins):
    ret_map = {}
    min_coins(amount, coins, ret_map)
    return ret_map

if __name__ == '__main__':
    print(min_coins_util(4, [1, 2, 3]))
