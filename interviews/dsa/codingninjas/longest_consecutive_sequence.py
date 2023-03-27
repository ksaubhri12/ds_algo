def longest_consecutive_sequence(arr: [], n: int):
    final_dict = {}
    for i in range(0, n):
        final_dict[arr[i]] = 0

    max_count = 0
    for key in final_dict.keys():
        count = 1
        if final_dict[key] == 0:
            final_dict[key] = 1
            look_up = key + 1
            while True:
                if look_up in final_dict:
                    final_dict[look_up] = 1
                    count = count + 1
                    max_count = max(count, max_count)
                    look_up = look_up + 1
                else:
                    break
    return max_count


if __name__ == '__main__':
    print(longest_consecutive_sequence([33, 20, 34, 30, 35], 5))
