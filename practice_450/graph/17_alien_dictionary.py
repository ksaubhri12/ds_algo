def get_order(word_list: [], k):
    adj_graph = get_relation_list(word_list, k)
    visited = [False] * k
    data_stack = []
    for i in range(k):
        if not visited[i]:
            dfs_util(i, visited, adj_graph, data_stack)
    final_arr = []
    while len(data_stack) > 0:
        pop_ele = data_stack.pop(-1)

        char_ele = chr(ord('a') + pop_ele)
        final_arr.append(char_ele)

    return final_arr


def dfs_util(vertex: int, visited: [], adj_graph: [[]], data_stack: []):
    if visited[vertex]:
        return
    visited[vertex] = True
    for neighbor in adj_graph[vertex]:
        dfs_util(neighbor, visited, adj_graph, data_stack)

    data_stack.append(vertex)


def get_relation_list(word_list: [], k):
    rel_arr = [[] for i in range(k)]
    i = 0
    n = len(word_list)

    while i < n - 1:
        first_word = word_list[i]
        second_word = word_list[i + 1]
        min_len = min(len(first_word), len(second_word))
        for j in range(min_len):
            if first_word[j] != second_word[j]:
                from_vertex = ord(first_word[j]) - ord('a')
                to_vertex = ord(second_word[j]) - ord('a')
                rel_arr[from_vertex].append(to_vertex)
                break

        i = i + 1

    return rel_arr


if __name__ == '__main__':
    print(get_order(["baa", "abcd", "abca", "cab", "cad"], 4))
    print(get_order(["caa", "aaa", "aab"], 3))
