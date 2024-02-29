def maxRootToLeafPathSum(root):
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    max_child_path_sum = max(maxRootToLeafPathSum(root.left, root.right))
    return root.val + max_child_path_sum

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        myset=set([0])
        for a,b in edges:
            if ((a==0 or b==0 or a in myset or b in myset) and (a not in restricted and b not in restricted)):
                myset.add(a)
                myset.add(b)
        return len(myset)
    
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        #building a undirected graph
        graph=collections.defaultdict(list)
        def buildgraph(edge):
            for x in edge:
                graph[x[0]].append(x[1])
                graph[x[1]].append(x[0])
        restricted=set(restricted)
        buildgraph(edges)

        #breadth first search of a graph
        count=0
        q=[]
        q.append(0)
        visited=[True]*n
        while q:
            cur=q[0]
            q.remove(cur)
            #if not visited,taken into account
            if visited[cur]:
                count+=1
                visited[cur]=False
            for x in graph[cur]:
                if visited[x] and x not in restricted :
                    q.append(x)
        return count