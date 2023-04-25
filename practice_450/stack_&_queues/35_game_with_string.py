from queue import PriorityQueue


def game_string(input_string: str, k):
    alphabet_map = {}
    for i in range(len(input_string)):
        char = input_string[i]
        alphabet_map[char] = alphabet_map[char] + 1 if char in alphabet_map else 1

    data_queue = PriorityQueue()
    for key in alphabet_map.keys():
        count = alphabet_map[key]
        data_queue.put(-count)

    for i in range(k):
        element = abs(data_queue.get())
        element = element - 1
        if element > 0:
            data_queue.put(-1 * element)

    answer = 0
    while len(data_queue.queue) > 0:
        element = data_queue.get()
        answer = answer + element ** 2

    return answer


if __name__ == '__main__':
    print(game_string('abccc', 1))
    print(game_string('aabcbcbcabcc', 3))
