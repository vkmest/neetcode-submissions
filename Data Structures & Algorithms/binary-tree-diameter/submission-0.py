# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path=0
        
        def depth(root):
            if root==None: return 0
            return 1 + max(depth(root.left), depth(root.right))
        
        def travel(root):
            if root==None: return

            nonlocal max_path
            max_path = max( max_path, depth(root.left)+depth(root.right))
            travel(root.left)
            travel(root.right)
        
        travel(root)
        return max_path