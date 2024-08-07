def is_power_of_two(x):
    return (x & (x - 1)) == 0


def counterGame(n):
    louise_turn = True

    while n > 1:
        if is_power_of_two(n):
            n //= 2
        else:
            largest_power_of_two = 1 << (n.bit_length() - 1)
            n -= largest_power_of_two

        louise_turn = not louise_turn

    return "Louise" if louise_turn else "Richard"
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            while (r-l+1) -max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            while (r-l+1) -max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]

        def backTracking(openN,closedN):
            if openN==closedN==n:
                res.append(''.join(stack))
                return
            if openN<n:
                stack.append('(')
                backTracking(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(')')
                backTracking(openN,closedN+1)
                stack.pop()

        backTracking(0,0)
        return res
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj={i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit=set()
        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j==prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0,-1) and n==len(visit)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par=[i for i in range(n)]
        rank = [1]*n
        def find(n1):
            res=n1
            while res !=par[res]:
                par[res]=par[par[res]]
                res=par[res]
            return res
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 ==p2:
                return 0
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p2]+=rank[p1]
            else:
                par[p2]=p1
                rank[p1]+=rank[p2]
            return 1
        res=n
        for n1,n2 in edges:
            res -=union(n1,n2)
        return res
        

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        for i,d in enumerate(temperatures):
            for j,d2 in enumerate(temperatures[i:]):
                if d2>d:
                    ans[i]=j
                    break
        return ans
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackInd=stack.pop()
                res[stackInd]=i-stackInd
            stack.append([t,i])

        return res
    
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[[p,s] for p,s in zip(position,speed)]
        stack=[]
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-2]>=stack[-1]:
                stack.pop()
        return len(stack)
    
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = []

        def addCell(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.pop(0)
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
