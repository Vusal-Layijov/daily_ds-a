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