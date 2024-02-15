from collections import deque


class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        while self.q:
            if self.q[0] >= t - 3000:
                break
            self.q.popleft()

        self.q.append(t)
        return len(self.q)
