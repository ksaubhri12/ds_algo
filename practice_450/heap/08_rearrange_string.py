from queue import PriorityQueue


def re_arrange_string(input_string: str):
    char_freq_map = {}
    n = len(input_string)
    for char in input_string:
        char_freq_map[char] = char_freq_map[char] + 1 if char in char_freq_map else 1

    data_queue = PriorityQueue()
    for key in char_freq_map:
        data_queue.put((char_freq_map[key] * -1, key))

    char_list = list(input_string)
    i = 0
    while len(data_queue.queue) > 0:
        element = data_queue.get()
        count = element[0] * -1
        char = element[1]
        if count > (n + 1) / 2:
            return ""
        for j in range(count):
            char_list[i] = char
            i = i + 2

            if i >= n:
                i = 1

    return ''.join(char_list)


if __name__ == '__main__':
    print(re_arrange_string('aab'))
    print(re_arrange_string('aaab'))
