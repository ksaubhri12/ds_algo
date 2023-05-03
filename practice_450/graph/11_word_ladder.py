def word_ladder(start_word, end_word, word_list):
    if start_word == end_word:
        return 0

    words_set = set(word_list)
    if end_word not in words_set:
        return 0
    word_size = len(start_word)
    data_queue = [start_word]
    steps = 0
    while len(data_queue) > 0:
        steps = steps + 1
        queue_size = len(data_queue)
        for i in range(queue_size):
            pop_word = data_queue.pop(0)
            pop_word_list = list(pop_word)
            for j in range(word_size):

                for k in range(26):
                    new_char_ord = ord('a') + k
                    new_char = chr(new_char_ord)
                    pop_word_list[j] = new_char
                    new_string = ''.join(pop_word_list)
                    if new_string == end_word:
                        return steps + 1
                    if new_string not in words_set:
                        continue

                    if new_string == pop_word:
                        continue

                    words_set.discard(new_string)
                    data_queue.append(new_string)
                pop_word_list = list(pop_word)
    return 0


if __name__ == '__main__':
    print(word_ladder('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
