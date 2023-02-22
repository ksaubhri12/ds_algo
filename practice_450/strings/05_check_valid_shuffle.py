def check_valid_shuffle(value_1, value_2, result):
    len_1 = len(value_1)
    len_2 = len(value_2)
    len_3 = len(result)
    if len_1 + len_2 != len_3:
        return False

    char_array_1 = [0] * 256
    char_array_2 = [0] * 256
    char_array_3 = [0] * 256

    set_char_array(value_1, char_array_1)
    set_char_array(value_2, char_array_2)
    set_char_array(result, char_array_3)

    answer = True
    for i in range(0, 256):
        count_in_val_1 = char_array_1[i]
        count_in_val_2 = char_array_2[i]
        count_in_val_3 = char_array_3[i]

        if count_in_val_1 + count_in_val_2 != count_in_val_3:
            answer = False
            break

    return answer


def set_char_array(value, char_array):
    for i in range(0, len(value)):
        element_order = ord(value[i])
        char_array[element_order] = char_array[element_order] + 1


if __name__ == '__main__':
    print(check_valid_shuffle("XY", "12", "1XY2"))
    print(check_valid_shuffle("XY", "12", "Y1X2"))
    print(check_valid_shuffle("XY", "12", "Y21XX"))
