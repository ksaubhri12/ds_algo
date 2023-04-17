def word_break_util(input_string, result_arr: [], input_dict: {}, output_string):
    if len(input_string) == 0:
        if output_string != '':
            result_arr.append(output_string)
        return

    n = len(input_string)

    for i in range(0, n):
        word = input_string[0:i + 1]
        if word in input_dict:
            word_break_util(input_string[i + 1:], result_arr, input_dict, output_string + str(word) + "-")


def word_break_main(input_string: [], input_dict: {}):
    result_arr = []
    word_break_util(input_string, result_arr, input_dict, '')
    final_arr = []
    for data in result_arr:
        result_words = data.split("-")[:-1]
        final_arr.append(' '.join(result_words))
    return final_arr


if __name__ == '__main__':
    word_dict = {'micro': 1, 'soft': 1, 'hi': 1, 'ring': 1, 'microsoft': 1, 'hiring': 1}
    print(word_break_main('microsofthiring', word_dict))
    word_dict = {"cats", "cat", "and", "sand", "dog"}
    print(word_break_main('catsanddog', word_dict))
    word_dict = {"cats", "cat", "and", "sand", "dog"}
    print(word_break_main('catsandog', word_dict))
