# We have to move all element by one place
# The last element will come at first place.
# Pick the first element and place it at first.
# Before doing it store first element in temp variable so that same can happen with second element
# Run the loop till n-2 since last element we know what is going to happen.

def cyclic_move_one_clock_wise(arr: [], n):
    last_element = arr[n - 1]
    temp = arr[0]
    for i in range(1, n - 1):
        element_to_pick = arr[i]
        arr[i] = temp
        temp = element_to_pick

    arr[n - 1] = temp
    arr[0] = last_element

    return arr


if __name__ == '__main__':
    print(cyclic_move_one_clock_wise([1, 2, 3, 4, 5], 5))
