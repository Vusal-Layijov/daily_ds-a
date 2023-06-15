def maxRootToLeafPathSum(root):
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    max_child_path_sum = max(maxRootToLeafPathSum(root.left, root.right))
    return root.val + max_child_path_sum