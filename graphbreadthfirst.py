adjList = {
    1: [2, 5],
    2: [1, 3, 5],
    3: [2, 4],
    4: [3, 5, 6],
    5: [1, 2, 4],
    6: [4]
}
def graphBreadtSearch(start):
    queue=[start]
    myset=set([start])
    result=[]
    while len(queue):
        current=queue.popleft()
        result.append(current)
        for neighbour in adjList[current]:
            if neighbour not in myset:
                queue.append(neighbour)
                myset.add(neighbour)
    return result

