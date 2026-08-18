# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True

        def traversal(root, left, right):
            if (root == None) or (self.valid == False):
                return
            if not (left < root.val < right):
                self.valid = False
                return
            if root.left:
                traversal(root.left, left, min(right, root.val))
            if root.right:
                traversal(root.right, max(left, root.val), right)


        traversal(root, float("-inf"), float("inf"))
        return self.valid