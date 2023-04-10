from typing import List


def max_possible_sum_stacks_util(stack_1: [], stack_2: [], stack_3: [], n1, n2, n3, sum_1, sum_2, sum_3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        return 0

    if sum_1 == sum_2 == sum_3:
        return sum_1

    min_sum = min(sum_1, sum_2, sum_3)
    if min_sum == sum_1 and min_sum != sum_2 and min_sum != sum_3:
        sum_2 = sum_2 - stack_2.pop(0)
        sum_3 = sum_3 - stack_3.pop(0)
        return max_possible_sum_stacks_util(stack_1, stack_2, stack_3, n1, n2 - 1, n3 - 1, sum_1, sum_2, sum_3)

    elif min_sum == sum_2 and min_sum != sum_3 and min_sum != sum_1:
        sum_1 = sum_1 - stack_1.pop(0)
        sum_3 = sum_3 - stack_3.pop(0)
        return max_possible_sum_stacks_util(stack_1, stack_2, stack_3, n1 - 1, n2, n3 - 1, sum_1, sum_2, sum_3)

    elif min_sum == sum_3 and min_sum != sum_1 and min_sum != sum_2:
        sum_2 = sum_2 - stack_2.pop(0)
        sum_1 = sum_1 - stack_1.pop(0)
        return max_possible_sum_stacks_util(stack_1, stack_2, stack_3, n1 - 1, n2 - 1, n3, sum_1, sum_2, sum_3)

    elif min_sum == sum_1 and min_sum == sum_2:
        sum_3 = sum_3 - stack_3.pop(0)
        return max_possible_sum_stacks_util(stack_1, stack_2, stack_3, n1, n2, n3 - 1, sum_1, sum_2, sum_3)

    elif min_sum == sum_1 and min_sum == sum_3:
        sum_2 = sum_2 - stack_2.pop(0)
        return max_possible_sum_stacks_util(stack_1, stack_2, stack_3, n1, n2 - 1, n3, sum_1, sum_2, sum_3)

    elif min_sum == sum_2 and min_sum == sum_3:
        sum_1 = sum_1 - stack_1.pop(0)
        return max_possible_sum_stacks_util(stack_1, stack_2, stack_3, n1 - 1, n2, n3, sum_1, sum_2, sum_3)

    else:
        return 0


def max_possible_sum_stack_driver(n1: int, n2: int, n3: int, s1: List[int], s2: List[int], s3: List[int]):
    return max_possible_sum_stacks_util(s1, s2, s3, n1, n2, n3, sum(s1), sum(s2), sum(s3))


if __name__ == '__main__':
    s1 = [4, 2, 3]
    s2 = [1, 1, 2, 3]
    s3 = [1, 4]
    # print(max_possible_sum_stack_driver(3, 4, 2, s1, s2, s3))

    s1 = [4, 7]
    s2 = [10]
    s3 = [1, 2, 3]
    # print(max_possible_sum_stack_driver(2, 1, 3, s1, s2, s3))

    s1 = [3, 1, 2]
    s2 = [5, 5, 3]
    s3 = [1, 2]
    print(max_possible_sum_stack_driver(3, 3, 2, s1, s2, s3))