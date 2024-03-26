def climbingLeaderboard(ranked, player):
    # Step 1: Create a unique ranked leaderboard
    unique_ranked = [ranked[0]]
    for score in ranked:
        if score != unique_ranked[-1]:
            unique_ranked.append(score)

    # Step 2: Initialize a list to store player ranks
    player_ranks = []

    # Step 3: Iterate through the player's scores
    for player_score in player:
        while unique_ranked and player_score >= unique_ranked[-1]:
            unique_ranked.pop()
        player_ranks.append(len(unique_ranked) + 1)

    return player_ranks


def anagram(s):
    # Write your code here
    if len(s)%2 !=0:
        return -1
    m=int(len(s)/2)
    w1=s[:m]
    w2=s[m:]
    print(w1,w2)
    count=0
    myList=list(w2)
    for l in w1:
        if l in myList:
            myList.remove(l)
        else:
            count+=1
    return count

#findSmallestSetOfVertices

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Set to keep track of nodes with incoming edges
        has_incoming_edge = set()
        
        # Populate the set with destination nodes of all edges
        for edge in edges:
            has_incoming_edge.add(edge[1])
            
        # The result is all nodes that don't have an incoming edge
        result = [node for node in range(n) if node not in has_incoming_edge]
        
        return result

#numIslands new
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        visited=set()
        R=len(grid)
        C=len(grid[0])
        def dfs(r,c):
            visited.add((r,c))
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in directions:
                if r+dr<R and dr+r >=0 and c+dc < C and c+dc>=0 and grid[r+dr][c+dc]=='1' and (r+dr,c+dc) not in visited:
                    dfs(r+dr,c+dc)
            return True

        for i in range(R):
            for j in range(C):
                if (i,j) not in visited and grid[i][j]=='1' and dfs(i,j):
                    count+=1
        return count