def print_valid_ip(string_value: str):
    result_arr = []


def print_util_min(string_value: str):
    return '.'.join(i for i in string_value)


def print_ip(string_value: str, len_needed, output_string: str):
    if len_needed <= 0:
        return output_string

    if len_needed == 1:
        return string_value

    if len_needed > len(string_value):
        return output_string

    if len_needed == len(string_value):
        return print_util_min(string_value)

    res = print_ip(string_value[1:], len_needed - 1, string_value[1:] + output_string)
    if res is not None:
        one_string = string_value[0] + "." + res
        print(one_string)

    res = print_ip(string_value[2:], len_needed - 2)
    if res is not None:
        two_string = string_value[0] + string_value[1] + "." + res
        print(two_string)

    res = print_ip(string_value[3:], len_needed - 3)
    if res is not None:
        three_string = string_value[0] + string_value[1] + string_value[2] + "." + res
        print(three_string)


def print_valid_ip_util(string_value: str):
    if len(string_value) < 4:
        return

    if len(string_value) == 4:
        print(print_util_min(string_value))
        return


def print_ip_v2(string_value, len_needed, output_string: str):
    if len_needed < 0:
        return

    if len_needed == 1:
        print(output_string + string_value)
        return

    if len_needed > len(string_value):
        # print(output_string + "." + string_value)
        return

    if len_needed == len(string_value):
        print(output_string + print_util_min(string_value))
        return

    print_ip_v2(string_value[1:], len_needed - 1, output_string + string_value[0] + ".")
    if len(string_value) > 2:
        print_ip_v2(string_value[2:], len_needed - 1, output_string + string_value[0] + string_value[1] + ".")
    if len(string_value) > 3:
        print_ip_v2(string_value[3:], len_needed - 1,
                    output_string + string_value[0] + string_value[1] + string_value[2] + ".")


if __name__ == '__main__':
    print(print_util_min('123'))
    print_ip_v2('12345', 4, '')
