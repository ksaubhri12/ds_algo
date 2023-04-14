def min_survival_days(days_to_survive, food_given_each_day, food_need_each_day):
    if food_given_each_day < food_need_each_day:
        return -1

    left_each_day = food_given_each_day % food_need_each_day
    if left_each_day * 6 < food_need_each_day and int(
            food_given_each_day // food_need_each_day) == 1 and days_to_survive > 6:
        return -1

    one_unit_days = food_given_each_day / food_need_each_day

    if days_to_survive % one_unit_days == 0:
        return int(days_to_survive // one_unit_days)
    else:
        return 1 + int(days_to_survive // one_unit_days)


if __name__ == '__main__':
    print(min_survival_days(5, 2, 2))
    print(min_survival_days(49, 16, 16))
    print(min_survival_days(10, 16, 2))
    print(min_survival_days(10, 20, 30))
