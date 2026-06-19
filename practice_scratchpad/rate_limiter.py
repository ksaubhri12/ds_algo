import time


class RateLimiter:
    def is_allowed(self, user_id) -> bool:
        pass


class FixedWindowRateLimiter(RateLimiter):

    def __init__(self, window_sec: int, limit: int):
        self.window = window_sec
        self.limit = limit
        self.counter = {}

    def is_allowed(self, user_id) -> bool:
        now = time.time()

        window_start = (now // self.window) * self.window

        if user_id not in self.counter:
            self.counter[user_id] = (0, window_start)

        count, curr_window = self.counter[user_id]
        if curr_window < window_start:
            count = 0

        if count >= self.limit:
            return False

        self.counter[user_id] = (count + 1, window_start)
        return True


class TokenBucketRateLimiter(RateLimiter):

    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.buckets = {}
        self.refill_rate = refill_rate  # token added per second

    def is_allowed(self, user_id) -> bool:
        now = time.time()

        if user_id not in self.buckets:
            self.buckets[user_id] = [self.capacity, now]
            self.buckets[user_id][0] = -1
            return True

        token, last_time = self.buckets[user_id]
        elapsed = now - last_time
        token = min(token + elapsed * self.refill_rate, self.capacity)

        if token < 1:
            self.buckets[user_id] = [token, now]
            return False

        self.buckets[user_id] = [token - 1, now]
        return True
