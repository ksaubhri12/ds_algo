import math


def max_product_sub_arr(arr: [], n):
    positive_product = 1
    zero_exist = False
    positive_exist = False
    negative_exist = False
    for i in range(0, n):
        if arr[i] > 0:
            positive_product = positive_product * arr[i]
            positive_exist = True
        if arr[i] == 0:
            zero_exist = True

        if arr[i] < 0:
            negative_exist = True

    if not positive_exist:
        positive_product = 0

    negative_element_count = 0
    negative_max_element = float('-inf')
    negative_product = 1
    for i in range(0, n):
        if arr[i] < 0:
            negative_element_count = negative_element_count + 1
            negative_max_element = max(negative_max_element, arr[i])
            negative_product = negative_product * arr[i]

    answer = None

    if negative_element_count == 1:
        if positive_exist:
            answer = positive_product
        elif zero_exist:
            answer = 0
        else:
            answer = negative_product

    elif negative_element_count % 2 == 0:
        answer = positive_product * negative_product

    else:
        best_from_negative = negative_product // negative_max_element
        answer = best_from_negative * positive_product

    if answer < 0:
        pro = -1
    else:
        pro = 1
    return pro * int(abs(answer) % (math.pow(10, 9) + 7))


if __name__ == '__main__':
    print(max_product_sub_arr([-1, -1, -2, 4, 3], 5))
    print(max_product_sub_arr([-5, 10, 7, 5, 7, 10], 6))
    print(max_product_sub_arr([-1], 1))
