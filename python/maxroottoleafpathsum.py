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