adjList = {
    1: [2, 5],
    2: [1, 3, 5],
    3: [2, 4],
    4: [3, 5],
    5: [1, 2, 4],
    6: []
}
def shortestPath(start,end):
    queue=[[start]]
    visited=set([start])
    print(queue)
    print(visited)
    while queue:
        curpath=queue.pop(0)
        curnode=curpath[len(curpath)-1]
        if curnode==end:
            return curpath
        for neighbour in adjList[curnode]:
            if neighbour not in visited:
                new=curpath+[neighbour]
                queue.append(new)
                visited.add(neighbour)
    return False
            

print(shortestPath(1,10))
