def min_flips(input_string: str):
    flip_start_with_1 = flip_string_start_with_word(input_string, '1')
    flip_start_with_0 = flip_string_start_with_word(input_string, '0')
    return min(flip_start_with_1, flip_start_with_0)


def flip_string_start_with_word(input_string: str, word):
    n = len(input_string)
    flip = 0
    for i in range(0, n):
        element = input_string[i]
        if element != word:
            flip = flip + 1

        if word == '1':
            word = '0'
        else:
            word = '1'

    return flip

if __name__ == '__main__':
    print(min_flips('001'))
