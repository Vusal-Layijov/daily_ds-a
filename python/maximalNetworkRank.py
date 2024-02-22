from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        road_count = {i: 0 for i in range(n)}
    # Create a set to quickly check if a road exists between two cities
        road_set = set()

    # Populate road_count and road_set
        for a, b in roads:
            road_count[a] += 1
            road_count[b] += 1
            road_set.add((a, b))
            road_set.add((b, a))

    # Calculate the maximal network rank
        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
            # Calculate network rank for the pair (i, j)
                rank = road_count[i] + road_count[j]
            # If there's a direct road between city i and j, adjust the rank
                if (i, j) in road_set:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank
    
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        stack=[]
        open='({['
        obj={")":"(","}":"{","]":"["}
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if stack and stack[-1]== obj[c]:
                    stack.pop()
                else:
                    stack.append(c)
        return False if stack else True


def beautifulTriplets(d, arr):
    # Write your code here
    count=0
    for num in arr:
        if num+d in arr and num + 2*d in arr:
            count+=1
    return count

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adjacency_list = defaultdict(list)
        for a, b in roads:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)            
        print(dict(adjacency_list))
        total_fuel_cost = [0]        
        def dfs(node, parent):
            people = 1            
            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    continue
                people += dfs(neighbor, node)                
            if node != 0:
                total_fuel_cost[0] += math.ceil(people / seats)                
            return people        
        dfs(0, None)
        return total_fuel_cost[0]

def getMaxFun(singer, length):
    # First, calculate initial fun without considering the order.
    unique_singers = len(set(singer))
    total_fun = sum(length) * unique_singers
    
    # Find the maximum fun by considering the decrement in fun
    # if a singer with more than one song appears earlier.
    # We sort by singer to group songs by the same singer together.
    combined = sorted(zip(singer, length), key=lambda x: (x[0], -x[1]))
    
    # Track seen singers to adjust the fun calculation.
    seen_singers = set()
    for s, l in combined:
        if s in seen_singers:
            # We already had this singer; calculate the reduction in fun.
            total_fun -= l
        else:
            seen_singers.add(s)
    
    return total_fun


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        adj2 = {}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
      
        for i in range(n):
            # add the node itself
            adj[i].append(i)
            adj[i].sort()
            adj2[i] = tuple(adj[i])
        
        res = 0
       
        print(adj2)
        print('ccccc', Counter(adj2.values()).items())
        for k, v in Counter(adj2.values()).items():
            res += 1 if len(k) == v else 0
        
        return res