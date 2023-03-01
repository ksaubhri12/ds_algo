def split_binary(value: str):
    n = len(value)
    first_element = value[0]
    last_element = first_element
    count = 0
    count = count + operation(last_element, first_element)
    pair = 0

    for i in range(1, n):
        element = value[i]
        count = count + operation(element, first_element)
        if count == 0:
            pair = pair + 1

    if pair == 0 or count != 0:
        return -1
    else:
        return pair


def operation(element, first_element):
    if element == first_element:
        return 1
    else:
        return -1


if __name__ == '__main__':
    print(split_binary('0100110101'))
    print(split_binary('0111100010'))
    print(split_binary('001110010'))
