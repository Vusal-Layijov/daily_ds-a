class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        minHeap=[(0,k)]
        visit=set()
        t=0
        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t=max(t,w1)
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2))
        return t if len(visit)==n else -1


def birthday(s, d, m):
    # Write your code here
    count = 0
    for ind in range(len(s)):
        if sum(s[ind:ind+m]) == d:
            count += 1
    return count
