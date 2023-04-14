# need to think and start again
from queue import PriorityQueue


class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


def max_job_profit(jobs: [Job], n):
    result = 0
    profit = 0
    jobs = sorted(jobs, key=lambda x: x.deadline)
    job_queue = PriorityQueue()
    for i in reversed(range(0, n)):
        if i == 0:
            slots_available = jobs[i].deadline
        else:
            slots_available = jobs[i].deadline - jobs[i - 1].deadline

        job_queue.put((-jobs[i].profit, jobs[i].deadline, jobs[i].id))

        while slots_available and len(job_queue.queue) > 0:
            element = job_queue.get()
            profit = profit + element[0] * -1
            slots_available = slots_available - 1
            result = result + 1

    return [result, profit]


if __name__ == '__main__':
    jobs_arr = [Job(1, 4, 20), Job(2, 1, 10), Job(3, 1, 40), Job(4, 1, 30)]
    print(max_job_profit(jobs_arr, 4))
