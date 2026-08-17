# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = []
        def traversal(root, lvl):
            if not root:
                return
            if len(self.levels)<=lvl:
                self.levels.append([])
            self.levels[lvl].append(root.val)
            traversal(root.left, lvl+1)
            traversal(root.right, lvl+1)
        traversal(root, 0)
        return self.levels