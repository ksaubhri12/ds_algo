def mirror_n_arr_tree(arr_1: [], arr_2: []):
    n = len(arr_1)
    m = len(arr_2)
    if n != m:
        return False
    node_element_dict = {}
    n = len(arr_1)
    i = 0
    while i < n:
        node = arr_1[i]
        connect_to = arr_1[i + 1]
        if node in node_element_dict:
            node_element_dict[node].append(connect_to)
        else:
            node_element_dict[node] = [connect_to]
        i = i + 2

    m = len(arr_2)
    j = 0
    answer = 1
    while j < m:
        node = arr_2[j]
        connect_to = arr_2[j + 1]
        if node not in node_element_dict:
            answer = 0
            break
        else:
            pop_element = node_element_dict[node].pop()
            if pop_element != connect_to:
                answer = 0
                break
        j = j + 2

    return answer


if __name__ == '__main__':
    print(mirror_n_arr_tree([1, 2, 1, 3], [1, 3, 1, 2]))
    arr_1 = [1, 2, 1, 3, 1, 4, 4, 5, 4, 6, 6, 7, 7, 8, 7, 9, 7, 10, 7, 11]
    arr_2 = [1, 4, 1, 3, 1, 2, 4, 6, 4, 5, 6, 7, 7, 11, 7, 10, 7, 9, 7, 8]
    print(mirror_n_arr_tree(arr_1, arr_2))
