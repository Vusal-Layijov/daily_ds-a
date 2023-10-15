class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        while self.requests and self.requests[0] < t-3000:
            self.requests.pop(0)
        self.requests.append(t)
        return len(self.requests)

def last_stone(stones):
    # Write your code here
    while len(stones)>=2:
        max1=max(stones)
        stones.remove(max1)
        max2=max(stones)
        stones.remove(max2)
        if max1==max2:
            continue
        stones.append(max1-max2)
    return stones[0] if len(stones)>0 else 0