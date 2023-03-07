def rearrange_characters_possible(input_string):
    n = len(input_string)
    alphabet_dict = {}
    for i in range(0, n):
        element = input_string[i]
        if element in alphabet_dict:
            alphabet_dict[element] = alphabet_dict[element] + 1
        else:
            alphabet_dict[element] = 1

    while len(alphabet_dict.keys()) > 0:
        max_count = 0
        alphabet_with_max_count = None

        for key in alphabet_dict.keys():
            count = alphabet_dict[key]
            if count > max_count:
                alphabet_with_max_count = key
