# The idea is to build a relation graph first
# then do a topological sorting
# to build a graph take two subsequent words
# and then when you find the first difference, just add that edge and break it
# after that it is nothing but a topological sort

def get_different_word(word_list):
    unique_letter = set()
    for word in word_list:
        for char in word:
            unique_letter.add(char)

    return len(unique_letter)


def get_order(word_list: []):
    k = get_different_word(word_list)
    adj_graph = get_relation_list(word_list)
    if dfs_detect_cycle(k, adj_graph):
        return ""

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
    if vertex in adj_graph:
        for neighbor in adj_graph[vertex]:
            dfs_util(neighbor, visited, adj_graph, data_stack)

    data_stack.append(vertex)


def get_relation_list(word_list: []):
    rel_arr = {}
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
                if from_vertex in rel_arr:
                    rel_arr[from_vertex].append(to_vertex)
                else:
                    rel_arr[from_vertex] = [to_vertex]
                break

        i = i + 1

    return rel_arr


def dfs_util_cycle(node, visited, path_visited, adj_graph) -> bool:
    visited[node] = True
    path_visited[node] = True

    if node in adj_graph:
        for neighbour in adj_graph[node]:
            if not visited[neighbour]:
                if dfs_util_cycle(neighbour, visited, path_visited, adj_graph):
                    return True
            elif path_visited[neighbour]:
                return True

    path_visited[node] = False
    return False


def dfs_detect_cycle(vertex, adj_graph) -> bool:
    visited = [False] * vertex
    path_visited = [False] * vertex
    for i in range(vertex):
        if not visited[i]:
            if dfs_util_cycle(i, visited, path_visited, adj_graph):
                return True

    return False


if __name__ == '__main__':
    # print(get_order(["baa", "abcd", "abca", "cab", "cad"]))
    # print(get_order(["ab", "cd", "ef", "ad"]))
    print(get_order(["a", "a", "a", "a", "aa", "aa", "aaa", "aaaaa", "aaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa"]))
