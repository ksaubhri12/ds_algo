from functools import cmp_to_key


class Solution:
    def activitySelection(self, n, start, end):
        return activity_selection_problem(n, start, end)


class MeetingStats:
    def __init__(self, index, start, end):
        self.index = index
        self.start = start
        self.end = end


def comparator(stats_1: MeetingStats, stats_2: MeetingStats):
    return stats_1.end - stats_2.end


def activity_selection_problem(n, start_arr: [], end_arr: []):
    stats_list = []
    for i in range(0, n):
        stats = MeetingStats(i + 1, start_arr[i], end_arr[i])
        stats_list.append(stats)

    stats_list = sorted(stats_list, key=cmp_to_key(comparator))
    result_list = [stats_list[0]]
    prev = stats_list[0]
    for i in range(1, len(stats_list)):
        current_event = stats_list[i]

        if current_event.start > prev.end:
            result_list.append(current_event)
            prev = current_event

    return len(result_list)


if __name__ == '__main__':
    print(Solution().activitySelection(4, [1, 3, 2, 5], [2, 4, 3, 6]))
