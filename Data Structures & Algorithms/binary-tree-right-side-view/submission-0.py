# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levels = []
        def traversal(root, cur_lvl):
            if not root:
                return
            if len(self.levels)<=cur_lvl:
                self.levels.append([])
            self.levels[cur_lvl].append(root.val)
            traversal(root.right, cur_lvl + 1)
            traversal(root.left, cur_lvl + 1)
        traversal(root, 0)
        right_nodes = [lvl[0] for lvl in self.levels]
        return right_nodes