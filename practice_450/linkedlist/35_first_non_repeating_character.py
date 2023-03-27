def first_non_repeating_character(stream: str):
    freq_dict = {}
    n = len(stream)
    visited = []
    answer = ''
    for i in range(0, n):
        char_value = stream[i]
        if char_value in freq_dict:
            freq_dict[char_value] = freq_dict[char_value] + 1
        else:
            freq_dict[char_value] = 1
            visited.append(char_value)

        m = len(visited)
        duplicate = True
        for j in range(0, m):
            if freq_dict[visited[j]] == 1:
                duplicate = False
                answer = answer + visited[j]
                break

        if duplicate:
            answer = answer + '#'

    return answer

if __name__ == '__main__':
    print(first_non_repeating_character('aabc'))
    print(first_non_repeating_character('aacb'))



