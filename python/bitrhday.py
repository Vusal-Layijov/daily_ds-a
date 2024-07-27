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
