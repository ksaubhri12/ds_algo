def get_starting_point(petrol_distance_data: [[]], n):
    start = 0
    extra_fuel = 0
    required_fuel = 0

    for i in range(n):
        extra_fuel = extra_fuel + petrol_distance_data[i][0] - petrol_distance_data[i][1]
        if extra_fuel < 0:
            required_fuel = required_fuel + extra_fuel
            extra_fuel = 0
            start = i + 1

    return start if extra_fuel + required_fuel >= 0 else -1


if __name__ == '__main__':
    stats = [[4, 6], [6, 5], [7, 3], [4, 5]]
    print(get_starting_point(stats, 4))
