"""
The last house is connected to the first house of this array
"""


def house_robber_tab(arr: []):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return 0
    without_first_house = arr[1:]
    without_last_house = arr[0:-1]
    money_without_first_house = house_robber_tab_util(without_first_house)
    money_without_last_house = house_robber_tab_util(without_last_house)
    return max(money_without_last_house, money_without_first_house)


def house_robber_tab_util(arr: []):
    n = len(arr)
    prev = arr[0]
    prev_prev = 0
    for i in range(1, n):
        pick = arr[i] + prev_prev
        non_pick = 0 + prev
        curr = max(pick, non_pick)
        prev_prev = prev
        prev = curr
    return prev


if __name__ == '__main__':
    print(house_robber_tab([9, 9, 1, 7, 5, 5, 1]))
    # print(house_robber_tab([2, 3, 2]))
