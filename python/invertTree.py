class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = [root]
        while len(queue) > 0:
            current = queue.pop(0)
            left = current.left
            current.left = current.right
            current.right = left

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root
