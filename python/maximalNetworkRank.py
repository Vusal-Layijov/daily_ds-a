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