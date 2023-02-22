def check_rotation(value_1, value_2):
    if len(value_1) != len(value_2):
        return False

    queue_1 = []
    queue_2 = []
    for i in range(0, len(value_1)):
        queue_1.append(value_1[i])

    for i in range(0, len(value_2)):
        queue_2.append(value_2[i])

    k = 0
    while k < len(queue_2):
        element_to_pop = queue_2.pop(0)
        queue_2.append(element_to_pop)
        if queue_2 == queue_1:
            return True
        k = k + 1

    return False


if __name__ == '__main__':
    print(check_rotation("ABCD", "CDAB"))
    print(check_rotation("ABCD", "ABCE"))
    print(check_rotation("ABCD", "ACBD"))
