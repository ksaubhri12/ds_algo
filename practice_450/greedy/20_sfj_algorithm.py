class Job:
    def __init__(self, arr_time, burst_time):
        self.arr_time = arr_time
        self.burst_time = burst_time
        self.completion_time = arr_time + burst_time
        self.waiting_time = arr_time
        self.tat = self.completion_time - self.arr_time


def sfj(arr_time: [], burst_time: [], n):
    stats_list = []
    for i in range(0, n):
        job = Job(arr_time[i], burst_time[i])
        stats_list.append(job)

    stats_list = sorted(stats_list, key=lambda x: (x.arr_time, x.burst_time))
    prev_job = stats_list[0]
    for i in range(1, n):
        job = stats_list[i]
        job.completion_time = prev_job.completion_time + job.burst_time
        job.waiting_time = job.completion_time - job.burst_time - job.arr_time
        job.tat = job.completion_time - job.arr_time
        prev_job = job

    waiting_time = 0
    tat = 0
    for i in range(0, n):
        waiting_time = waiting_time + stats_list[i].waiting_time
        tat = tat + stats_list[i].tat
    avg_waiting_time = round(waiting_time / n, 2)
    avg_tat = round(tat / n, 2)
    return [avg_waiting_time, avg_tat]


if __name__ == '__main__':
    print(sfj([12, 29, 25, 22, 4, 24, 29, 10, 11], [26, 11, 14, 3, 21, 6, 28, 29, 7], 9))
    print(sfj([1, 0, 4], [13, 12, 25], 3))
