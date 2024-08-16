class Node:
    def __init__(self, val=0, neighbors=None) -> None:
        self.val =val
        self.neighbors=neighbors if neighbors is not None else []
def cloneGraph(node):
    oldToNew={}
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        copy=Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    return dfs(node) if node else None


class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        l=r=0
        while r<len(nums)-1:
            f=0
            for i in range(l,r+1):
                f=max(f,nums[i]+i)
            l=r+1
            r=f
            res+=1
        return res

def preOrder(root):
    #Write your code here
    if not root:
        return
    print(root.info, end=' ')
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)
def postOrder(root):
    #Write your code here
    if not root:
        return
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print(root.info, end=' ')