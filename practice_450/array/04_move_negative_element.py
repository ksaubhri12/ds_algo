def move_negative_element(arr: [], n):
    positive_arr = []
    negative_arr = []

    for i in range(0, n):
        element = arr[i]
        if element < 0:
            negative_arr.append(element)
        else:
            positive_arr.append(element)

    for i in range(0, len(negative_arr)):
        positive_arr.append(negative_arr[i])

    return positive_arr


if __name__ == '__main__':
    print(move_negative_element([-8 ,9, 5, 10, 2, 6, -7, 7], 8))
