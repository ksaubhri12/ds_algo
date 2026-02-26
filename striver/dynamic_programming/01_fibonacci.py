def fibonaci(n):
    if n <= 1:
        return n
    return fibonaci(n - 1) + fibonaci(n - 2)


def fibonaci_mem(n):
    mem_table = {}
    return fibonaci_mem_rec(n, mem_table)


def fibonaci_mem_rec(n, mem_table):
    if n <= 1:
        return n
    if n in mem_table:
        return mem_table[n]
    mem_table[n] = fibonaci_mem_rec(n - 1, mem_table) + fibonaci_mem_rec(n - 2, mem_table)
    return mem_table[n]


def fibonaci_table(n):
    table_arr = [-1] * (n + 1)
    table_arr[0] = 0
    table_arr[1] = 1
    for i in range(2, n + 1):
        table_arr[i] = table_arr[i - 1] + table_arr[i - 2]
    return table_arr[n]


if __name__ == '__main__':
    # print(fibonaci(100))
    print(fibonaci_mem(100))
    print(fibonaci_table(100))
