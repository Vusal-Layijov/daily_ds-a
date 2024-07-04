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