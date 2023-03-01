def equivalent_mobile_keypad(input_string: str):
    data = {'A': "2", 'B': "22", 'C': "222",
            'D': "3", 'E': "33", 'F': "333",
            'G': "4", 'H': "44", 'I': "444",
            'J': "5", 'K': "55", 'L': "555",
            'M': "6", 'N': "66", 'O': "666",
            'P': "7", 'Q': "77", 'R': "777", 'S': "7777",
            'T': "8", 'U': "88", 'V': "888",
            'W': "9", 'X': "99", 'Y': "999", 'Z': "9999", ' ': '0'}

    output_string = ''
    n = len(input_string)
    for i in range(0, n):
        element = input_string[i]
        value = data[element]
        output_string = output_string + value

    return output_string


if __name__ == '__main__':
    print(equivalent_mobile_keypad('HELLO WORLD') == '4433555555666096667775553')
    print(equivalent_mobile_keypad('GEEKSFORGEEKS') == '4333355777733366677743333557777')
