from collections import defaultdict


def build_graph(cities):
    edges = defaultdict(list)
    for source, dest in cities:
        edges[source].append(dest)
        edges[dest].append(source)    
    return edges


def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited


def roadsAndLibraries(n, c_lib, c_road, cities):

    if c_lib <= c_road:
        return c_lib * n

    edges = build_graph(cities)
    covered = set()
    cost = 0

    # main logic
    for node in range(1, n + 1):
        if node not in covered:

            # split graphs into components
            city_group = dfs(set(), edges, node)

            # add costs for connecting cities + cost of 1 lib
            roads_to_build = len(city_group)-1
            cost += roads_to_build * c_road
            cost += c_lib

            # should not consider any of these cities again
            for city in city_group:
                covered.add(city)

    return cost


def kangaroo(x1, v1, x2, v2):
    if v2 >= v1 or (x2 - x1) % (v1 - v2) != 0:
        return "NO"
    return "YES"

#get Total


def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    check = []
    for num in range(a[-1], b[0]+1):
        check.append(num)
    go1 = []
    for i in check:
        if all(map(lambda x: i % x == 0, a)):
            go1.append(i)
    go2 = []
    for j in go1:
        if all(map(lambda x: x % j == 0, b)):
            go2.append(j)
    return len(go2)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        res = 0
        visit = set()
        minH = [[0, 0]]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res
