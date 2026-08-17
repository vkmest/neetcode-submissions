# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        def traversal(root, maxi):
            if not root: 
                return
            if root.val >= maxi:
                self.good_nodes +=1
            traversal(root.left, max(root.val, maxi))
            traversal(root.right, max(root.val, maxi))

        traversal(root, root.val)
        return self.good_nodes