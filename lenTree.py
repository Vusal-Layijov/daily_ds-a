class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        count = 0
        queue = [root]

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            count += 1
        return count
