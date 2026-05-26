import copy
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


def find_sequences(start_word, end_word, word_list):
    queue = Queue()
    queue.put([start_word])
    word_set = set(word_list)
    used_on_level = set()
    used_on_level.add(start_word)
    level = 0

    ans = []
    while len(queue.queue) > 0:
        item_popped = queue.get()
        if len(item_popped) > level:
            level += 1
            for element in used_on_level:
                if element in word_set:
                    word_set.remove(element)

        curr_word = item_popped[-1]
        if curr_word == end_word:
            # first sequence
            if len(ans) == 0:
                ans.append(item_popped)
            elif len(ans[0]) == len(item_popped):
                ans.append(item_popped)

        for neighbour in word_neighbour(curr_word):
            if neighbour in word_set:
                item_popped.append(neighbour)
                used_on_level.add(neighbour)
                queue.put(copy.deepcopy(item_popped))
                item_popped.pop()
    return ans


if __name__ == '__main__':
    print(find_sequences("der", "dfs", ["des", "der", "dfr", "dgt", "dfs"]))
