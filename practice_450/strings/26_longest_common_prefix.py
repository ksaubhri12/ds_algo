def longest_common_prefix(arr: []):
    n = len(arr)
    min_word = arr[0]
    min_word_arr_len = len(min_word)
    for i in range(0, n):
        word = arr[i]
        len_word = len(word)
        if len_word < min_word_arr_len:
            min_word_arr_len = len_word
            min_word = word

    longest_prefix = ''
    for i in range(0, min_word_arr_len):
        prefix = min_word[0: min_word_arr_len - i]
        answer = True
        for j in range(0, n):
            if not find_word_in_string_with_prefix_condition(prefix, arr[j]):
                answer = False
                break
        if answer:
            longest_prefix = prefix
            break
    return longest_prefix


def find_word_in_string_with_prefix_condition(word, input_string):

    m = len(word)
    sub_string = input_string[0:m]
    return word == sub_string


if __name__ == '__main__':
    print(longest_common_prefix(["reflower","flow","flight"]))
    print(longest_common_prefix(["flower", "flow", "flight"]))
    print(longest_common_prefix(["dog", "racecar", "car"]))
    print(longest_common_prefix(["a"]))
    # print(find_word_in_string('flo', 'flower'))
    # print(find_word_in_string('ca', 'flower'))
    # print(find_word_in_string('flow', 'caterflowkast'))
