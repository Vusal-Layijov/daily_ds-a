def roadsAndLibraries(n, c_lib, c_road, cities):
    # Construct adjacency list
    adjacency_list = []
    print(cities)
    for i in range(n+1):
        adjacency_list += [[]]
    for i in range(len(cities)):
        adjacency_list[cities[i][0]].append(cities[i][1])
        adjacency_list[cities[i][1]].append(cities[i][0])
    print('a list', adjacency_list)
    city_grouop_count = []
    visited = []
    for i in range(n+1):
        visited.append(False)

    # Count number of cities in each connected set
    for group in range(1, n+1):
        if len(adjacency_list[group]) > 0 and not visited[group]:
            city_grouop_count.append(dfs(adjacency_list, group, visited))
        elif len(adjacency_list[group]) == 0:
            city_grouop_count.append(1)

    # Add the lowest cost for 1) either connecting each set of cities and building one library or 2) building a library in each city
    ans = 0
    for i in range(len(city_grouop_count)):
        ans += min((city_grouop_count[i] - 1) *
                   c_road + c_lib, city_grouop_count[i] * c_lib)
    return ans


def dfs(adjacency_list, group, visited):
    visited[group] = True
    ans = 1
    for i in range(len(adjacency_list[group])):
        neighbor = adjacency_list[group][i]
        if not visited[neighbor]:
            ans += dfs(adjacency_list, neighbor, visited)
    return ans
