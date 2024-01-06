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