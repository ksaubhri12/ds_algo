def palindromic_partition_helper(input_string: str, output_string: str, result_arr: []):
    if len(input_string) == 0:
        result_arr.append(output_string)
        return

    n = len(input_string)
    for i in range(0, n):
        word = input_string[0:i + 1]
        ros = input_string[i + 1:]
        if is_palindrome(word):
            palindromic_partition_helper(ros, output_string + word + "-", result_arr)


def is_palindrome(word):
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start = start + 1
        end = end - 1

    return True


def print_partition(input_word):
    result_arr = []
    input_dict = {}
    palindromic_partition_helper(input_word, '', result_arr)
    final_arr = []
    for data in result_arr:
        sub_string = data.split('-')[:-1]
        final_arr.append(sub_string)
    return final_arr


if __name__ == '__main__':
    print(print_partition('pep'))
    print(print_partition('madam'))
    print(print_partition('geeks'))
    print(print_partition('wwwzz'))
