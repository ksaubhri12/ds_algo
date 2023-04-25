def min_arrow(input_arr: []):
    if len(input_arr) == 0:
        return 0

    n = len(input_arr)
    c = 1
    arrow_map = {input_arr[0] - 1: 1}

    for i in range(1, n):
        height_need = input_arr[i]
        if height_need in arrow_map and arrow_map[height_need] > 0:
            arrow_map[height_need] = arrow_map[height_need] - 1
        else:
            c = c + 1
            new_height = input_arr[i] - 1
            if new_height in arrow_map:
                arrow_map[new_height] = arrow_map[new_height] + 1
            else:
                arrow_map[new_height] = 1

    return c


if __name__ == '__main__':
    print()
