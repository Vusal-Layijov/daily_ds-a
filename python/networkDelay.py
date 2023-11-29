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


#equal Chocolate
def equal(arr):
    # Store all the possibilities
    possibilities = [0] * 5

    # Start with the minimum element
    minimum = min(arr)

    for _ in range(len(possibilities)):
        for k in arr:
            diff = k - minimum
            steps_required = diff // 5 + \
                (diff % 5) // 2 + ((diff % 5) % 2) // 1
            possibilities[_] += steps_required
        minimum -= 1

    # Return the minimum number out of all the possibilities
    return min(possibilities)
