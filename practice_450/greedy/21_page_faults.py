def page_faults(n, c, pages):
    lru_map = {}
    lru_queue = []
    lru_size = 0
    fault = 0
    for i in range(0, n):
        page = pages[i]
        if page not in lru_map:
            fault = fault + 1
            if lru_size < c:
                lru_queue.append(page)
                lru_size = lru_size + 1
                lru_map[page] = lru_size - 1

            else:
                front = lru_queue.pop(0)
                lru_size = lru_size - 1
                del lru_map[front]
                lru_queue.append(page)
                lru_size = lru_size + 1
                lru_map[page] = lru_size - 1
                for j in range(0, len(lru_queue)):
                    lru_map[lru_queue[j]] = j

        else:
            index = lru_map[page]
            lru_queue = lru_queue[0:index] + lru_queue[index + 1:]
            lru_queue.append(page)
            lru_map[page] = lru_size - 1
            for j in range(0, len(lru_queue)):
                lru_map[lru_queue[j]] = j

    return fault


if __name__ == '__main__':
    print(page_faults(20, 4, [1, 1, 3, 2, 5, 4, 5, 3, 1, 4, 4, 1, 5, 2, 1, 4, 5, 3, 3, 3]))

    print(page_faults(18, 3, [4, 1, 1, 5, 2, 1, 4, 1, 5, 4, 5, 4, 4, 5, 4, 3, 4, 4]))
    print(page_faults(19, 18, [5, 3, 2, 4, 4, 4, 5, 1, 5, 2, 1, 1, 3, 5, 2, 5, 1, 2, 5]))
    print(page_faults(17, 7, [5, 3, 2, 3, 1, 1, 2, 1, 3, 5, 4, 1, 3, 4, 1, 1, 1]))

    print(page_faults(16, 12, [4, 4, 3, 1, 3, 1, 4, 1, 4, 2, 5, 1, 4, 1, 2, 5]))

    # print(page_faults(9, 4, [5, 0, 1, 3, 2, 4, 1, 0, 5]))
    # print(page_faults(4, 3, [1, 3, 2, 1]))
    # print(page_faults(5, 3, [1, 2, 3, 4, 3]))
