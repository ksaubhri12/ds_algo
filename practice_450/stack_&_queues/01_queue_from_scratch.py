class Queue:

    def __init__(self):
        self.queue_arr = []

    def isEmpty(self):
        if len(self.queue_arr) == 0:
            return 1
        else:
            return -1

    def enqueue(self, data):
        self.queue_arr.append(data)
        return data

    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue_arr.pop(0)

    def front(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue_arr[0]
