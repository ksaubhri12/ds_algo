def could_not_get_computer(n, input_string: str):
    normal_dict = {}
    not_get_dict = {}

    final_result = []
    computer_number = n
    total_customer = len(input_string)
    for i in range(0, total_customer):
        customer_name = input_string[i]
        if customer_name in normal_dict:
            del normal_dict[customer_name]
            computer_number = computer_number + 1
        else:
            if computer_number > 0:
                normal_dict[customer_name] = 1
                computer_number = computer_number - 1
            else:
                not_get_dict[customer_name] = 1
                final_result.append(customer_name)

    return list(not_get_dict.keys())


if __name__ == '__main__':
    print(could_not_get_computer(2, 'ABBAJJKZKZ'))
    print(could_not_get_computer(3, 'GACCBDDBAGEE'))
    print(could_not_get_computer(3, 'GACCBGDDBAEE'))
    print(could_not_get_computer(1, "ABCBCA"))
    print(could_not_get_computer(1, 'ABCBCADEED'))
