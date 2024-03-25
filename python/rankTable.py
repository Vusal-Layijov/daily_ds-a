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