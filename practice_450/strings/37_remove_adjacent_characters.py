def remove_adjacent_characters(input_string):
    final_string = input_string[0]
    n = len(input_string)
    for i in range(1, n):
        if input_string[i] != input_string[i - 1]:
            final_string = final_string + input_string[i]

    return final_string


if __name__ == '__main__':
    print(remove_adjacent_characters('aabb'))
    print(remove_adjacent_characters('aabaa'))
