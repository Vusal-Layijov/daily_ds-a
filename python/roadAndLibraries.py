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
