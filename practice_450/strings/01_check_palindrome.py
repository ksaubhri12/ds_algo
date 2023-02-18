def check_palindrome(value: str):
    n = len(value)
    result = True
    start = 0
    end = n - 1

    while start <= end:
        if value[start] != value[end]:
            result = False
        start = start + 1
        end = end - 1

    return result


if __name__ == '__main__':
    print(check_palindrome('abba'))
    print(check_palindrome('aba'))
