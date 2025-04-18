import math
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        print(prerequisites)
        preMap={i:[] for i in range(numCourses)}
        visit=set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs]==[]:
                return True
            visit.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            visit.remove(crs)
            preMap[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preMap={c:[] for c in range(numCourses)}
        visit=set()
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        res=[]
        cycle=set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) ==False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return res 

def stockMax(prices):
    profit=0
    maxP=0
    for price in prices[::-1]:
        if price>maxP:
            maxP=price
        else:
            profit+=maxP-price
    return profit


def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

    
# Complete the redJohn function below.
def redJohn(n):
    maxHorizontals = n // 4
    M = 0
    for i in range(maxHorizontals + 1):
        simplifiedN = n - (i * 3)        
        # Using formula "simplifiedN CHOOSE i"
        M += int(math.factorial(simplifiedN) / (math.factorial(i) * math.factorial(simplifiedN - i)))
        
    ans = 0
    for i in range(M + 1):
        if i > 1 and is_prime(i):
            ans += 1
    return ans

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par=[i for i  in range(len(edges)+1)]
        rank=[1]*(len(edges)+1)
        def find(n):
            p=par[n]
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                rank[p1]+=rank[p2]
                par[p2]=p1
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
def funnyString(s):
    # Write your code here
    r=s[::-1]
    print(s,r)
    res=[]
    for ind in range(len(s)):
        res.append(abs(ord(s[ind]) - ord(r[ind])))
    
    return "Funny" if len(set(res))==1 else 'Not Funny'

def flatlandSpaceStations(n, c):
    if n == len(c): return 0
    if 1 == len(c): return max(c[0], n-1-c[0])
    
    c = sorted(c)
    
    if c[0] == 0:
        maxDist = 0
    else:
        maxDist = c[0]*2

    if c[-1] != n-1:
        maxDist = max(maxDist, ((n-1)-c[-1])*2)
    last = 0
    for i in c:
        maxDist = max((i-last), maxDist)
        last = i

    return maxDist//2

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
        
    
def hackerrankInString(s):
    # Write your code here
    myList=list(s)
    myList.append(0)
    for l in 'hackerrank':
        if l in myList:
            ind=myList.index(l)
            myList=myList[ind+1:]
        else:
            return 'NO'
    return 'YES'

class Solution:
    def divisorGame(self, n: int) -> bool:
        forMod=1
        first=False
        while n>1:
            for x in range(1,n):
                if n%x==0:
                    n=n-x
                    break
            first = not first
        return first
    
def maxSubarray(arr):
    # Maximum subsequence sum
    maxsq = max(arr)  # In case all numbers are negative, pick the largest
    if maxsq > 0:  # If there are positive numbers, sum them
        maxsq = sum(num for num in arr if num > 0)
    else:
        # All numbers are negative, so we don't need to sum; maxsq is already the maximum number
        pass
    
    # Maximum subarray sum using Kadane's Algorithm
    max_ending_here = max_so_far = arr[0]
    for num in arr[1:]:
        # max_ending_here keeps track of the sum of the subarray ending at the current position
        # It is either the current number itself or the current number plus the previous max_ending_here, whichever is larger
        max_ending_here = max(num, max_ending_here + num)
        # max_so_far keeps track of the largest sum we have seen so far
        max_so_far = max(max_so_far, max_ending_here)
    
    return (max_so_far, maxsq)

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.hlpr(nums[1:]),self.hlpr(nums[:-1]))
    def hlpr(self, nums: List[int]) -> int:
        rob1=0
        rob2=0
        
        for i  in range(len(nums)):
            tmp=nums[i]+rob1
            rob1=rob2
            rob2=max(tmp,rob2)
        return rob2

        
        
class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            res+=self.countP(s,i,i)
            res+=self.countP(s,i,i+1)
        return res

    def countP(self, s,l,r):
        res=0
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1
        return res

        

        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        res = []

        for src, dst in tickets:
            adj[src].append(dst)

        for key in adj:
            adj[key].sort()

        def dfs(adj, result, src):
            if src in adj:
                destinations = adj[src][:]
                while destinations:
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(adj, res, dest)
                    destinations = adj[src][:]
            res.append(src)

        dfs(adj, res, "JFK")
        res.reverse()

        if len(res) != len(tickets) + 1:
            return []

        return res
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums+nums
    
def passwordCracker(passwords, loginAttempt):
    def backtrack(remaining_attempt, path):
        if not remaining_attempt:
            return path
        for password in passwords:
            if remaining_attempt.startswith(password):
                result = backtrack(remaining_attempt[len(password):], path + [password])
                if result:
                    return result    
        return None

    result = backtrack(loginAttempt, [])
    if result:
        return ' '.join(result)
    else:
        return 'WRONG PASSWORD'


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)
    
# Buttom up
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            if i<len(s)-1 and (s[i]=="1" or (s[i]=='2' and s[i+1] in "0123456") ) :
                dp[i]+=dp[i+2]
        return dp[0]