def merge_overlapping_intervals(intervals: [[]]):
    n = len(intervals)
    intervals = sorted(intervals, key=lambda x: x[0])
    final_interval_list = []
    curr_start_interval = intervals[0][0]
    curr_end_interval = intervals[0][1]
    final_interval_list.append([curr_start_interval, curr_end_interval])

    for i in range(1, n):
        curr_interval = final_interval_list.pop(-1)
        curr_start_interval = curr_interval[0]
        curr_end_interval = curr_interval[1]

        interval = intervals[i]
        next_start_time = interval[0]
        next_end_timer = interval[1]

        if next_start_time <= curr_end_interval:
            final_end = max(next_end_timer, curr_end_interval)
            final_start = curr_start_interval
            final_interval_list.append([final_start, final_end])

        else:
            final_interval_list.append([curr_start_interval, curr_end_interval])
            final_interval_list.append([next_start_time, next_end_timer])

    return final_interval_list


if __name__ == '__main__':
    print(merge_overlapping_intervals([[1, 3], [2, 4], [6, 8], [9, 10]]))
    print(merge_overlapping_intervals([[6, 8], [1, 9], [2, 4], [4, 7]]))
