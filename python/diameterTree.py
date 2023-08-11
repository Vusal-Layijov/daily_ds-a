class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depth(node, diameter):
            if not node:
                return 0
            l_dep = depth(node.left, diameter)
            r_dep = depth(node.right, diameter)
            diameter[0] = max(diameter[0], l_dep+r_dep)
            return max(l_dep, r_dep) + 1
        diameter = [0]
        depth(root, diameter)
        return diameter[0]
