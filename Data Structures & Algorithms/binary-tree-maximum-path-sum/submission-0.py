# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        result = root.val 
        def dfs(node):
            nonlocal result
            if node is None:
                return 0
            
            leftg = max(0, dfs(node.left))
            rightg = max(0, dfs(node.right))

            result = max (result, node.val + leftg + rightg)

            return node.val + max(leftg, rightg)  # what we are returning to parent

        dfs(root)
        return result