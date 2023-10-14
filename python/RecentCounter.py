class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        while self.requests and self.requests[0] < t-3000:
            self.requests.pop(0)
        self.requests.append(t)
        return len(self.requests)
