from queue import Queue


def word_neighbour(word) -> []:
    possible_combination = []
    word_len = len(word)
    for char_index in range(word_len):
        char = word[char_index]
        for i in range(26):
            new_char = chr(i + ord('a'))
            if new_char != char:
                new_word = word[0:char_index] + new_char + word[char_index + 1:]
                possible_combination.append(new_word)

    return possible_combination


def word_ladder(start_word, end_word, word_list):
    visited = set()
    word_list = set(word_list)
    queue = Queue()
    queue.put([start_word, 1])
    visited.add(start_word)
    while len(queue.queue) > 0:
        item_popped = queue.get()
        curr_word = item_popped[0]
        curr_level = item_popped[1]
        if curr_word == end_word:
            return curr_level

        for neighbour in word_neighbour(curr_word):
            if neighbour in word_list and neighbour not in visited:
                visited.add(neighbour)
                queue.put([neighbour, curr_level + 1])

    return 0


if __name__ == '__main__':
    print(word_ladder("der", "dfs", ["des", "der", "dfr", "dgt", "dfs"]))
    print(word_ladder("gedk", "geek", ["geek", "gefk"]))
