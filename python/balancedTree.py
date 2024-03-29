import collections
def balancedTree(root):
    def dfs(root):
        if not root:
            return [True,0]
        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
        return [balanced, max(left[1],right[1])+1]
    return dfs(root)[0]

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res =[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res
    

    def validPath(self, n: int, edges: List[List[int]], src: int, des: int) -> bool:
        graph = [[] for _ in range(n)]
        for edge in edges:
            src1, des1 = edge
            src2, des2 = edge[::-1]
            graph[src1].append(des1)
            graph[src2].append(des2)
        
        visited = set()
        def has_path(node):
            if node == des:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if has_path(neighbor):
                        return True
            return False
        return has_path(src)
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=nums.copy()
        for ind in range(2,len(nums)):
            dp[ind]=max(max(dp[0:ind]),nums[ind]+dp[ind-2], nums[ind]+max(dp[0:ind-1]))
        print(dp)
        return max(dp)
    
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = collections.defaultdict(set)
        for u, v in edges:
            d[u].add(v)
            d[v].add(u)
        s = set(range(n))
        while len(s) > 2:
            leaves = set(i for i in s if len(d[i]) == 1)
            s -= leaves
            for i in leaves:
                for j in d[i]:
                    d[j].remove(i)
        return list(s)

def jeanisRoute(k, roads, cities):
    g, start, cities = collections.defaultdict((dict)), cities[0], set(cities)
    for i,j , w in roads:
        g[i][j] = g[j][i] = w 
    visited = set()
    ans = [0, 0]
    def dfs(node, dis = 0):
        visited.add(node)
        isBelong = node in cities
        minus = [0,0]
        for i, val in g[node].items():
            if i not in visited:
                d = dfs(i, dis+val) - dis
                if d > 0:
                    isBelong = True
                    ans[0] += 2 * g[node][i]
                    if d > minus[0]:
                        minus[1], minus[0] = max(minus), d
                    else: minus[1] = max(minus[1], d)
        ans[1] = max(ans[1], sum(minus)) 
        return dis + max(minus) if isBelong else 0
    dfs(start) 
    return ans[0] - ans[1]
print(jeanisRoute(3,[[1, 2, 1], [2, 3, 2], [2, 4, 2], [3, 5, 3]],[1,3,4]))