from heapq import heappush, heappop

def shortestReach(n, edges, s):
    
    g = [set() for _ in range(n+1)]
    for u, v, w in edges:
        g[u].add((v, w))
        g[v].add((u, w))

    queue = [(0, s)]
    bag = {s: 0}
    processed = [-1] * (n+1)
    
    while queue:
        
        cost, u = heappop(queue)
        
        if processed[u] != -1: continue
        processed[u] = cost
        
        for v, w in g[u]:
            if processed[v] == -1:
                curr_cost = bag.get(v, float("inf"))
                new_cost = cost + w
                if curr_cost > new_cost:
                    heappush(queue, (new_cost, v))
                    bag[v] = new_cost
    
    return processed[1:s] + processed[s+1:]

def candies(n, arr):
    # Initialize an array to store the number of candies for each child
    candies_count = [1] * n

    # Traverse the ratings from left to right
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies_count[i] = candies_count[i - 1] + 1

    # Traverse the ratings from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies_count[i] = max(candies_count[i], candies_count[i + 1] + 1)

    # The total number of candies is the sum of candies for all children
    return sum(candies_count)