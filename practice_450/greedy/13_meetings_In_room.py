def max_meeting_in_room(n, start: [], end: []):
    meeting_stats = []
    for i in range(0, n):
        meeting_stats.append([start[i], end[i]])

    meeting_stats = sorted(meeting_stats, key=comparator)

    count = 1
    prev_end = meeting_stats[0][1]
    for i in range(1, n):
        curr_meeting = meeting_stats[i]
        start = curr_meeting[0]
        end = curr_meeting[1]
        if start > prev_end:
            count = count + 1
            prev_end = end

    return count


def comparator(meeting_stat):
    return meeting_stat[1]


if __name__ == '__main__':
    print(max_meeting_in_room(6, [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
    print(max_meeting_in_room(3, [10, 12, 20], [20, 25, 30]))
