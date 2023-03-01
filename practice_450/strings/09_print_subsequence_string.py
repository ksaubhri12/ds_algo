def print_subsequence(value: str, output: str):
    if len(value) == 0:
        print(output)
        return

    print_subsequence(value[1:], output + value[0])

    print_subsequence(value[1:], output)


if __name__ == '__main__':
    print_subsequence('a', '')
    print_subsequence('ab', '')
    print_subsequence('abc', '')
