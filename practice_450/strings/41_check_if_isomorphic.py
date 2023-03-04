def check_if_isomorphic(str_1: str, str_2: str):
    if len(str_1) != len(str_2):
        return False
    n = len(str_1)
    mapping_dict = {}

    answer = True
    for i in range(0, n):
        element_in_str_1 = str_1[i]
        element_in_str_2 = str_2[i]
        if element_in_str_1 in mapping_dict:
            map_value = mapping_dict[element_in_str_1]
            if map_value != element_in_str_2:
                answer = False
                break

        else:
            if element_in_str_2 in mapping_dict.values():
                answer = False
                break
            else:
                mapping_dict[element_in_str_1] = element_in_str_2

    return answer



if __name__ == '__main__':
    print(check_if_isomorphic('aab', 'xqu'))
    print(check_if_isomorphic('aab', 'xxy'))
    print(check_if_isomorphic('aba', 'xyy'))
    print(check_if_isomorphic('aba', 'xxx'))
