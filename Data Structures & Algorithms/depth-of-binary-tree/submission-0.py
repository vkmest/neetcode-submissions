# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth=0

        def deep(root, depth):
            if root==None: return

            nonlocal max_depth
            max_depth=max(max_depth, depth)

            deep(root.left, depth+1)
            deep(root.right, depth+1)
            return

        deep(root, 1)
        return max_depth