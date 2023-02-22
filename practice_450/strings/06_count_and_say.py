def count_and_say(n):
    if n == 1:
        return '1'
    return say_v2(count_and_say(n - 1))


def say(string: str):
    dict_count = {}
    for i in range(0, len(string)):
        char_value = string[i]
        if char_value in dict_count:
            dict_count[char_value] = dict_count[char_value] + 1
        else:
            dict_count[char_value] = 1

    final_string = ''
    for key in dict_count.keys():
        count = dict_count[key]
        element = str(count) + key
        final_string = final_string + element

    return final_string


def say_v2(string: str):
    final_string = ''
    element = string[0]
    count = 1
    for i in range(1, len(string)):
        curr_element = string[i]
        if curr_element != element:
            string_add = str(count) + string[i - 1]
            element = curr_element
            count = 1
            final_string = final_string + string_add
        else:
            count = count + 1
    if count >= 1:
        final_string = final_string + str(count) + element

    return final_string


if __name__ == '__main__':
    print(count_and_say(4))
    print(count_and_say(5))
    # print(say_v2('1'))
    # print(say_v2('11'))
    print(say_v2('21'))
    print(say_v2('1211'))

    # print(say('111'))
    # print(say('211'))
