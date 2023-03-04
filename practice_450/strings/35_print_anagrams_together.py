def print_anagrams_together(words: [str], n: int):
    sorted_words_arr_dict = {}
    for i in range(0, n):
        element = words[i]
        sorted_element_arr = sorted(element)
        sorted_element_str = "".join([str(j) for j in sorted_element_arr])
        if sorted_element_str in sorted_words_arr_dict:
            sorted_words_arr_dict[sorted_element_str].append(i)
        else:
            sorted_words_arr_dict[sorted_element_str] = [i]

    final_answer = []
    for key in sorted_words_arr_dict:
        anagram_word_index = sorted_words_arr_dict[key]
        internal_list = []
        for j in range(0, len(anagram_word_index)):
            internal_list.append(words[anagram_word_index[j]])
        final_answer.append(internal_list)

    return final_answer


if __name__ == '__main__':
    print(print_anagrams_together(['act', 'god', 'cat', 'dog', 'tac'], 5))
