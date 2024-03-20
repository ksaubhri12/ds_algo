# fibonacci
import time


def fibonacci_recursion(n):
    if n in (0, 1):
        return n
    result = fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)
    return result


def fibonacci_rec_util(n):
    result = []
    for i in range(n):
        ret = fibonacci_recursion(i)
        result.append(ret)
    return result


def fibonacci_rec_mem(n, ret_map: {}):
    if n in ret_map:
        return ret_map[n]
    if n in (0, 1):
        ret_map[n] = n
        return n
    ret = fibonacci_rec_mem(n - 1, ret_map) + fibonacci_rec_mem(n - 2, ret_map)
    ret_map[n] = ret
    return ret


def fibonacci_rec_mem_util(n):
    ret_map = {}
    fibonacci_rec_mem(n, ret_map)
    result = []
    for i in range(n):
        result.append(ret_map[i])
    return list(result)


def fibonacci_tab(n):
    result = [-1] * (n + 1)
    result[0] = 0
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i - 1] + result[i - 2]
    return result


def fibonacci_tab_opt(n):
    if n in (0, 1):
        return n
    prev = 0
    prev_prev = 1
    result = None
    for i in range(2, n + 1):
        result = prev + prev_prev
        prev_prev = prev
        prev = result

    return result


if __name__ == '__main__':
    print(fibonacci_tab_opt(100))
    start = time.time()
    print(fibonacci_tab(100)[-2])
    print("TIME_TAKEN TAB : {}".format(time.time() - start))
    start = time.time()
    print(fibonacci_rec_mem_util(100)[-1])
    print("TIME_TAKEN REC_MEM : {}".format(time.time() - start))
    start = time.time()
    print(fibonacci_rec_util(37)[-1])
    print("TIME_TAKEN : {}".format(time.time() - start))
