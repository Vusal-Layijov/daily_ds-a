def canFinish(numCourses,prerequisites):
    preMap={i:[] for i in range(numCourses)}
    for crs,pre in prerequisites:
        preMap[crs].append(pre)
    visitSet=set()
    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs]==[]:
            return True
        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): return False
        
        visitSet.remove(crs)
        preMap[crs]=[]
        return True
    for crs in range(numCourses):
        if not dfs(crs): return False
    return True

def hurdleRace(k, height):
    # Write your code here
    maxX=max(height)
    return maxX-k if maxX>k else 0


def angryProfessor(k, a):
    # Write your code here
    c=0
    for aS in a:
        if aS <=0:
            c+=1
    return 'NO' if c>=k else 'YES'

def beautifulDays(i, j, k):
    # Write your code here
    res=[]
    for num in range(i,j+1):
        r=str(num)
        new=int(r[::-1])
        print(new)
        if (num-new) % k==0:
            res.append(new)
    
    return len(res)

def viralAdvertising(n):
    # Write your code here
    cum=2
    curr=2
    for i in range(n-1):
        get=curr*3
        newC=get//2
        cum+=newC
        curr=newC
    return cum


def circularArrayRotation(a, k, queries):
    for _ in range(k):
        for i in range(len(a)-1,0,-1):
            tmp=a[i]
            a[i]=a[i-1]
            a[i-1]=tmp
            
    return a

def jumpingOnClouds(c, k):
    energy = 100
    index = 0
    while True:
        index = (index + k) % len(c)
        if c[index] == 1:
            energy -= 3
        else:
            energy -= 1
        if index == 0:
            break
    return energy
def findDigits(n):
    count = 0
    new = str(n)
    for d in new:
        if int(d) != 0 and n % int(d) == 0:
            count += 1
    return count
def appendAndDelete(s, t, k):    
    diff = 0
    shorter = min(len(s), len(t))
    for i in range(shorter):
        if s[i] != t[i] or i == shorter - 1:
            diff = i
            break    
    count = len(s) - diff + len(t) - diff
    if count <= k and (count - k) % 2 == 0:
        return "Yes"
    elif len(s) + len(t) <= k:
        return "Yes"
    else:
        return "No"
def squares(a, b):
    # Write your code here
    count=0
    for num in range(a,b+1):
        root=num**0.5
        if root.is_integer():
            count +=1
    return count
def cutTheSticks(arr):
    # Write your code here
    res=[]
    while len(arr)>0:
        res.append(len(arr))
        mini=min(arr)
        arr=[x-mini for x in arr if x-mini>0]
    return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        if(len(nums)==1):
            return [nums[:]]
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
        
    
def repeatedString(string, n):
    # Write your code here
    count_a = 0
    if n<len(string):
        count_a = string[:n%len(string)].count('a')
    else:
        count_a = string.count('a') + int(n/len(string)-1)*string.count('a')
        if n%len(string)>0:
            count_a+=string[0:n%len(string)].count('a')
    return count_a


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(i,subset):
            if i==len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1,subset)
        backtrack(0,[])
        return res
def roadsInHackerland(n, roads):
    # Initialize the distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # Fill the distance matrix with road lengths
    for u, v, w in roads:
        dist[u-1][v-1] = 2**w  # Convert road length to power of 2
        dist[v-1][u-1] = 2**w

    # Floyd-Warshall algorithm to find shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Sum up the distances
    total_distance = sum(dist[i][j] for i in range(n) for j in range(i+1, n))

    # Convert the sum to binary representation
    return bin(total_distance)[2:]
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            if node == len(graph) - 1:
                result.append(path)
                return
            for next_node in graph[node]:
                dfs(next_node, path + [next_node])
                print(path)
                
        result = []
        dfs(0, [0])
        return result