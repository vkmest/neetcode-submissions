# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = 0

        def traversal(root, less):
            if (not root) or (self.res != 0): return less

            left = traversal(root.left, less)
            if (self.res != 0): return left
            
            less = left + 1

            if less == self.k:
                self.res = root.val
                return less
                
            right = traversal(root.right, less)
            return right

        traversal(root, 0)
        return self.res