import heapq
def minPower(cells):
    # Write your code here
    heapq.heapify(cells)  # Transform list into a heap
    power = 0

    while len(cells) > 1:
        min1 = heapq.heappop(cells)  # Pop the smallest element
        min2 = heapq.heappop(cells)  # Pop the next smallest element
        add = min1 + min2
        power += add
        heapq.heappush(cells, add)  # Push the sum back into the heap

    return power