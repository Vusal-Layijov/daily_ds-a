def birthday(s, d, m):
    # Write your code here
    result = 0
    for ind in range(len(s)):
        if ind + m <= len(s):
            if sum(s[ind:ind+m]) == d:
                result += 1
    return result

#pickNumbers

def pickingNumbers(a):
    # Write your code here
    finalSet = 0
    a.sort()
    for i in a:
        previousSet = 0
        for j in a:
            if i == j or (j - i) == 1:
                previousSet += 1
        if previousSet > finalSet:
            finalSet = previousSet
    return finalSet
#bfs 

def bfs(n,m,edges,s):
    vis=[False for i in range(n+1)]
    dis = {i:-1 for i in range(n+1)}
    adj=[[] for i in range(n+1)]
    for item in edges:
        adj[item[0]].append(item[1])
        adj[item[1]].append(item[0])
    dis[s]=0
    vis[s]=True
    q=[s]
    while q:
        cur=q.pop(0)
        for nei in adj[cur]:
            if not vis[nei]:
                dis[nei]=6+dis[cur]
                q.append(nei)
                vis[nei]=True

    del dis[0]
    del dis[s]
    return list(dis.values())

            
#get ways
def getWays(n, c):
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(len(c)):
        for j in range(c[i], n + 1):
            table[j] += table[j - c[i]]
    return table[n]

def largestPermutation(k, arr):
    n = len(arr)
    pos = {num: i for i, num in enumerate(arr)}
    
    for i in range(n):
        if k <= 0:
            break
        valueToPlace = n - i
        if arr[i] == valueToPlace:
            continue
        posToPlace = pos[valueToPlace]
        
        # Swap the values in the array
        arr[i], arr[posToPlace] = arr[posToPlace], arr[i]
        
        # Update the positions in the dictionary
        pos[arr[posToPlace]], pos[arr[i]] = pos[arr[i]], pos[arr[posToPlace]]
        
        k -= 1
    
    return arr

# Example usage
k = 2
arr = [4, 2, 3, 5, 1]
print(largestPermutation(k, arr))  # Output: [5, 4, 3, 2, 1]
def topView(root):
    if not root:
        return

    # Dictionary to store the top view nodes with horizontal distance as key
    top_view = {}
    
    # Array-based queue for level order traversal; stores pairs of node and its horizontal distance
    queue = [(root, 0)]  # (node, horizontal distance)
    
    while queue:
        node, hd = queue.pop(0)  # Simulate dequeue operation by popping from the front
        
        # If the horizontal distance is not in top_view, add the node's info to it
        if hd not in top_view:
            top_view[hd] = node.info

        # Add left child to queue with HD - 1
        if node.left:
            queue.append((node.left, hd - 1))

        # Add right child to queue with HD + 1
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Extract and sort keys to print the top view in the correct order
    sorted_hd_keys = sorted(top_view.keys())
    print(" ".join(str(top_view[hd]) for hd in sorted_hd_keys))
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.validPalindromeUtil(s, i + 1, j) or self.validPalindromeUtil(s, i, j - 1)
        return True
    
    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True