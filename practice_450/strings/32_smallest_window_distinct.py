def smallest_distinct_window(input_string):
    start = 0
    end = 1
    alphabet_dict = {}

    distinct_list = list(set(input_string))
    for i in range(0, len(distinct_list)):
        alphabet_dict[distinct_list[i]] = 0
    n = len(distinct_list)
    count = 1
    alphabet_dict[input_string[0]] = 1
    answer = len(input_string)
    while start <= end < len(input_string):
        if count < n:
            element = input_string[end]
            if alphabet_dict[element] == 0:
                alphabet_dict[element] = 1
                count = count + 1
            else:
                alphabet_dict[element] = alphabet_dict[element] + 1
            end = end + 1
        elif count == n:
            answer = min(answer, end - start)
            element = input_string[start]
            if element in alphabet_dict and alphabet_dict[element] == 1:
                count = count - 1
            alphabet_dict[element] = alphabet_dict[element] - 1
            start = start + 1

    while count == n:
        answer = min(answer, end - start)
        element = input_string[start]
        if element in alphabet_dict and alphabet_dict[element] == 1:
            count = count - 1
        alphabet_dict[element] = alphabet_dict[element] - 1
        start = start + 1

    return answer


if __name__ == '__main__':
    print(smallest_distinct_window('aabcbcdbca'))
