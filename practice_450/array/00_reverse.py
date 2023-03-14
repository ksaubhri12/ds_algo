# Take pointer from left
# Take pointer from right
# Replace the value
# Increase both the pointer by one one in their direction.
# Loop will run till n/2


def reverse_array(arr: [], n: int):
    for i in range(0, int(n / 2)):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

    return arr


if __name__ == '__main__':
    print(reverse_array([1, 2, 3, 4, 5], 5))

    print(reverse_array([1, 2, 3, 4, 5, 6], 6))
