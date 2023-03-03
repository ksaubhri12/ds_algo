def first_repeated_word(input_string: str):
    words_arr = input_string.split(' ')
    word_dict = {}
    answer = 'No word'
    for i in range(0, len(words_arr)):
        word = words_arr[i]
        if word in word_dict:
            answer = word
        else:
            word_dict[word] = 1

        if answer != 'No word':
            break

    return answer


if __name__ == '__main__':
    print(first_repeated_word('Ravi had been saying that he had been there'))
